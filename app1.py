import os
import sys
import threading
import time
import subprocess
import sqlite3
from datetime import datetime
from dateutil import tz
from flask import Flask, request, jsonify, render_template_string

# -------------------------
DB = "home_monitor.db"
MAX_RECENT = 200
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -------------------------
TSHARK_FIELDS = [
    "frame.time_epoch",
    "eth.src",
    "ip.src",
    "ip.dst",
    "ip.version",
    "dns.qry.name",
    "http.host",
    "ssl.handshake.extensions_server_name"
]

# -------------------------
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS observations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts TEXT,
        src_mac TEXT,
        src_ip TEXT,
        ip_version INTEGER,
        proto TEXT,
        domain TEXT,
        sha256 TEXT
    )
    """)
    conn.commit()
    conn.close()

def sha256_bytes(b: bytes):
    import hashlib
    return hashlib.sha256(b).hexdigest()

def store_observation(ts, mac, ip, ipver, proto, domain):
    raw = f"{ts}|{mac}|{ip}|{ipver}|{proto}|{domain}".encode()
    sha = sha256_bytes(raw)
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO observations (ts, src_mac, src_ip, ip_version, proto, domain, sha256) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (ts, mac, ip, ipver, proto, domain, sha)
    )
    conn.commit()
    conn.close()

# -------------------------
class TSharkRunner(threading.Thread):
    def __init__(self, iface=None, pcap=None):
        super().__init__(daemon=True)
        self.iface = iface
        self.pcap = pcap
        self.proc = None
        self.stop_flag = threading.Event()

    def run(self):
        cmd = ["tshark", "-l", "-T", "fields"]
        for f in TSHARK_FIELDS:
            cmd += ["-e", f]
        cmd += ["-E", "separator=\t", "-E", "occurrence=f"]
        if self.pcap:
            cmd += ["-r", self.pcap]
        elif self.iface:
            cmd += ["-i", self.iface, "-Y", "dns || http.request || ssl.handshake.extensions_server_name"]
        else:
            print("No iface or pcap provided")
            return

        try:
            self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, bufsize=1)
        except FileNotFoundError:
            print("tshark not found. Please install tshark.", file=sys.stderr)
            return

        for line in self.proc.stdout:
            if self.stop_flag.is_set():
                break
            line = line.rstrip("\n")
            if not line:
                continue
            cols = line.split("\t")
            while len(cols) < len(TSHARK_FIELDS):
                cols.append("")
            try:
                ts_epoch = cols[0]
                eth_src = cols[1] or None
                ip_src = cols[2] or None
                ip_dst = cols[3] or None
                ip_ver = int(cols[4]) if cols[4] else None
                dns_q = cols[5] or None
                http_host = cols[6] or None
                sni = cols[7] or None

                domain = None
                proto = None
                if dns_q:
                    domain = dns_q.rstrip(".")
                    proto = "DNS"
                elif http_host:
                    domain = http_host
                    proto = "HTTP"
                elif sni:
                    domain = sni
                    proto = "TLS-SNI"

                ts = datetime.fromtimestamp(float(ts_epoch), tz=tz.tzlocal()).isoformat() if ts_epoch else datetime.now(tz=tz.tzlocal()).isoformat()

                if domain:
                    store_observation(ts, eth_src, ip_src, ip_ver, proto, domain)

            except Exception as e:
                continue

    def stop(self):
        self.stop_flag.set()
        if self.proc:
            try:
                self.proc.terminate()
            except:
                pass

# -------------------------
# Flask Web App
# -------------------------
app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Home Domain Monitor</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{padding:16px}
.table-sm td, .table-sm th{padding:.3rem;font-size:.85rem}
</style>
</head>
<body>
<div class="container">
  <h2>Home Domain Monitor</h2>

  <div class="row mb-3">
    <div class="col-md-6">
      <form id="uploadForm" method="POST" action="/upload" enctype="multipart/form-data">
        <div class="input-group">
          <input type="file" name="pcap" accept=".pcap,.pcapng" class="form-control" required>
          <button class="btn btn-primary" type="submit">Upload PCAP</button>
        </div>
      </form>
    </div>
    <div class="col-md-6 text-end">
      <button id="refreshBtn" class="btn btn-sm btn-outline-secondary" onclick="refreshAll()">Refresh</button>
    </div>
  </div>

  <div class="row">
    <div class="col-md-5">
      <h5>Devices (MAC/IP)</h5>
      <table class="table table-sm table-bordered" id="devicesTbl">
        <thead><tr><th>Device</th><th>Unique domains</th></tr></thead>
        <tbody></tbody>
      </table>
    </div>
    <div class="col-md-7">
      <h5>Top Domains</h5>
      <canvas id="domainChart" height="120"></canvas>
      <h5 class="mt-3">Recent Observations</h5>
      <table class="table table-sm table-bordered">
        <thead><tr><th>Time</th><th>Device (MAC/IP)</th><th>Proto</th><th>Domain</th></tr></thead>
        <tbody id="recent"></tbody>
      </table>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
let chart = null;
async function refreshAll(){
  const res = await fetch('/api/summary');
  const j = await res.json();

  const tbody = document.querySelector('#devicesTbl tbody'); tbody.innerHTML = '';
  j.devices.forEach(d=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><b>${d.device}</b><div class="text-muted small">${d.sample_ip||''}</div></td><td>${d.count}</td>`;
    tbody.appendChild(tr);
  });

  const labels = j.top_domains.map(x=>x[0]);
  const data = j.top_domains.map(x=>x[1]);
  if(chart) chart.destroy();
  const ctx = document.getElementById('domainChart').getContext('2d');
  chart = new Chart(ctx, {type:'bar', data:{labels:labels, datasets:[{label:'count', data:data}]}, options:{responsive:true, plugins:{legend:{display:false}}}});

  const rtb = document.getElementById('recent'); rtb.innerHTML = '';
  j.recent.forEach(it=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${it.ts}</td><td>${it.src_mac||it.src_ip}</td><td>${it.proto}</td><td>${it.domain}</td>`;
    rtb.appendChild(tr);
  });
}
setInterval(refreshAll, 3000);
refreshAll();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(INDEX_HTML)

@app.route("/api/summary")
def api_summary():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # recent
    c.execute("SELECT ts, src_mac, src_ip, proto, domain FROM observations ORDER BY id DESC LIMIT 60")
    rows = c.fetchall()
    recent = [{"ts": r[0], "src_mac": r[1], "src_ip": r[2], "proto": r[3], "domain": r[4]} for r in rows]
    # top domains
    c.execute("SELECT domain, COUNT(*) as cnt FROM observations WHERE domain IS NOT NULL GROUP BY domain ORDER BY cnt DESC LIMIT 12")
    top = c.fetchall()
    # devices
    c.execute("SELECT COALESCE(src_mac, src_ip) as dev, COUNT(DISTINCT domain) FROM observations GROUP BY dev ORDER BY COUNT(DISTINCT domain) DESC LIMIT 50")
    devs = c.fetchall()
    devices = [{"device": d[0], "count": d[1], "sample_ip": None} for d in devs]
    conn.close()
    return jsonify({"recent": recent, "top_domains": top, "devices": devices})

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("pcap")
    if not f:
        return "No file", 400
    path = os.path.join(UPLOAD_DIR, f.filename)
    f.save(path)
    # スレッドでPCAP解析
    def analyze_uploaded():
        runner = TSharkRunner(pcap=path)
        runner.run()
    threading.Thread(target=analyze_uploaded, daemon=True).start()
    return "Uploaded; analysis started. Return to dashboard.", 200

# -------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--iface", help="capture interface for live mode")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    init_db()

    if args.iface:
        runner = TSharkRunner(iface=args.iface)
        runner.start()

    app.run(host="0.0.0.0", port=8080, debug=False)
