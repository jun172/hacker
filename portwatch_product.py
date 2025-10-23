#!/usr/bin/env python3
# portwatch_product.py
"""
PortWatch MVP
- auto-scan (nmap) -> sqlite -> Flask UI
- new-port detection -> webhook (HTTPS) optionally via proxy
- WARNING: run only on targets you own or are authorized to scan
"""

import os
import sqlite3
import subprocess
import xml.etree.ElementTree as ET
import json
import threading
import time
from datetime import datetime
from flask import Flask, render_template_string, request, redirect, url_for, jsonify, flash

import requests

# ---------------- Config ----------------
TARGETS = os.getenv("PW_TARGETS", "127.0.0.1").split(",")  # comma separated
SCAN_INTERVAL = int(os.getenv("PW_SCAN_INTERVAL", "300"))   # seconds
NMAP_ARGS = os.getenv("PW_NMAP_ARGS", "-sV -p- --version-intensity 1")
DB_PATH = os.getenv("PW_DB", "portwatch_scans.db")
WEBHOOK_URL = os.getenv("PW_WEBHOOK")  # e.g. https://example.com/webhook
# Optional proxies for outbound webhook (requests format)
# Example: http://127.0.0.1:3128
PROXY_URL = os.getenv("PW_PROXY")  # set to proxy URL or leave empty
PROXIES = {"http": PROXY_URL, "https": PROXY_URL} if PROXY_URL else None

# SQLite schema
SCHEMA = """
CREATE TABLE IF NOT EXISTS hosts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  scan_time TEXT,
  address TEXT
);
CREATE TABLE IF NOT EXISTS ports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  host_id INTEGER,
  port INTEGER,
  protocol TEXT,
  state TEXT,
  service TEXT,
  banner TEXT,
  confidence INTEGER,
  FOREIGN KEY(host_id) REFERENCES hosts(id)
);
CREATE INDEX IF NOT EXISTS idx_ports_port ON ports(port);
CREATE INDEX IF NOT EXISTS idx_hosts_address ON hosts(address);
"""

# ---------- Utilities ----------
def ensure_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    conn.commit()
    return conn

def run_nmap_xml(target, extra_args=NMAP_ARGS, timeout=300):
    cmd = f"nmap {extra_args} -oX - {target}"
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0 and not proc.stdout:
        # even if returncode != 0, sometimes stdout contains partial results; handle carefully
        raise RuntimeError(f"nmap failed: {proc.stderr.strip()[:200]}")
    return proc.stdout

def parse_nmap_xml(xmltxt):
    root = ET.fromstring(xmltxt)
    results = []
    for host in root.findall('host'):
        addr = None
        for a in host.findall('address'):
            if a.get('addr'):
                addr = a.get('addr')
        host_elem = {"address": addr, "ports": []}
        ports = host.find('ports')
        if ports is None:
            results.append(host_elem)
            continue
        for p in ports.findall('port'):
            portnum = int(p.get('portid'))
            protocol = p.get('protocol')
            state = p.find('state').get('state') if p.find('state') is not None else ''
            service = p.find('service')
            svcname = service.get('name') if service is not None and service.get('name') else ''
            product = service.get('product') if service is not None and service.get('product') else ''
            version = service.get('version') if service is not None and service.get('version') else ''
            extrainfo = service.get('extrainfo') if service is not None and service.get('extrainfo') else ''
            banner = " ".join([v for v in (svcname, product, version, extrainfo) if v]).strip()
            host_elem['ports'].append({
                "port": portnum,
                "protocol": protocol,
                "state": state,
                "service": svcname,
                "product": product,
                "version": version,
                "extrainfo": extrainfo,
                "banner": banner
            })
        results.append(host_elem)
    return results

COMMON_MAP = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",
    21: "FTP",
    25: "SMTP",
    3389: "RDP",
    389: "LDAP",
    8080: "HTTP-alt",
}

def enrich_ports(parsed):
    for h in parsed:
        for p in h['ports']:
            likely = COMMON_MAP.get(p['port'], "")
            b = (p.get('banner') or "").lower()
            if 'apache' in b: likely = likely or 'Apache'
            elif 'nginx' in b: likely = likely or 'Nginx'
            elif 'microsoft-iis' in b or 'iis' in b: likely = likely or 'IIS'
            elif 'mysql' in b: likely = likely or 'MySQL'
            elif 'postgres' in b: likely = likely or 'PostgreSQL'
            p['likely'] = likely
            # confidence heuristic
            conf = 0
            if p['service']: conf += 30
            if p['banner']: conf += 40
            if p['likely']: conf += 30
            if p['state'] != 'open': conf = 0
            p['confidence'] = conf
    return parsed

def store_results(conn, parsed):
    cur = conn.cursor()
    scan_time = datetime.utcnow().isoformat() + "Z"
    for h in parsed:
        addr = h.get('address')
        cur.execute("INSERT INTO hosts(scan_time,address) VALUES(?,?)", (scan_time, addr))
        host_id = cur.lastrowid
        for p in h['ports']:
            cur.execute("""INSERT INTO ports(host_id,port,protocol,state,service,banner,confidence)
                           VALUES(?,?,?,?,?,?,?)""",
                        (host_id, p['port'], p['protocol'], p['state'], p['service'], p['banner'], p['confidence']))
    conn.commit()

def latest_scan_for(conn, address):
    cur = conn.cursor()
    cur.execute("SELECT id, scan_time FROM hosts WHERE address=? ORDER BY id DESC LIMIT 1", (address,))
    row = cur.fetchone()
    if not row:
        return None
    host_id, scan_time = row
    cur.execute("SELECT port, protocol, state, service, banner, confidence FROM ports WHERE host_id=? ORDER BY port", (host_id,))
    ports = [dict(zip(['port','protocol','state','service','banner','confidence'], r)) for r in cur.fetchall()]
    return {"scan_time": scan_time, "address": address, "ports": ports}

def detect_new_ports(conn, parsed):
    alarms = []
    for h in parsed:
        addr = h.get('address')
        cur = conn.cursor()
        cur.execute("SELECT id FROM hosts WHERE address=? ORDER BY id DESC LIMIT 1", (addr,))
        prev = cur.fetchone()
        prev_ports = set()
        if prev:
            prev_id = prev[0]
            cur.execute("SELECT port FROM ports WHERE host_id=?", (prev_id,))
            prev_ports = set([r[0] for r in cur.fetchall()])
        current_ports = set([p['port'] for p in h['ports'] if p['state']=='open'])
        new_ports = sorted(list(current_ports - prev_ports))
        if new_ports:
            alarms.append({"address": addr, "new_ports": new_ports, "timestamp": datetime.utcnow().isoformat() + "Z"})
    return alarms

def notify_webhook(payload):
    if not WEBHOOK_URL:
        return False
    headers = {"Content-Type":"application/json"}
    try:
        r = requests.post(WEBHOOK_URL, json=payload, headers=headers, timeout=8, proxies=PROXIES)
        return r.status_code < 300
    except Exception as e:
        print("Webhook send error:", e)
        return False

# ---------- Scanner thread ----------
class ScannerThread(threading.Thread):
    def __init__(self, conn):
        super().__init__(daemon=True)
        self.conn = conn
        self._stop = threading.Event()

    def run(self):
        while not self._stop.is_set():
            for t in TARGETS:
                t = t.strip()
                try:
                    xml = run_nmap_xml(t)
                    parsed = parse_nmap_xml(xml)
                    parsed = enrich_ports(parsed)
                    alarms = detect_new_ports(self.conn, parsed)
                    store_results(self.conn, parsed)
                    if alarms:
                        for a in alarms:
                            print("ALARM:", a)
                        notify_webhook({"alarms": alarms})
                except Exception as e:
                    print("Scan error for", t, ":", e)
            # sleep between full-target rounds
            for _ in range(int(SCAN_INTERVAL)):
                if self._stop.is_set(): break
                time.sleep(1)

    def stop(self):
        self._stop.set()

# ---------- Flask UI ----------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")  # for flash only; do not use in prod

DB_CONN = ensure_db()
scanner = ScannerThread(DB_CONN)
scanner.start()

INDEX_HTML = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>PortWatch</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="p-4">
<div class="container">
  <h1>PortWatch</h1>
  <p class="text-muted">Targets: {{ targets|join(', ') }}</p>
  <div class="mb-3">
    <form method="post" action="{{ url_for('manual_scan') }}">
      <button class="btn btn-primary">今すぐスキャン</button>
    </form>
    <a class="btn btn-secondary" href="{{ url_for('show_history') }}">履歴一覧</a>
  </div>

  {% if latest %}
    <h5>最新: {{ latest.scan_time }} ({{ latest.address }})</h5>
    <p>Open ports:</p>
    <ul>
      {% for p in latest.ports %}
        <li>
          <strong>{{ p.port }}</strong> ({{ p.service or 'unknown' }}) — {{ p.banner or '-' }} — confidence: {{ p.confidence }}
          {% if p.likely %} <span class="badge bg-info">{{ p.likely }}</span>{% endif %}
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <div class="alert alert-warning">No scans yet.</div>
  {% endif %}

  <hr>
  <h5>Top Open Ports</h5>
  <canvas id="topChart" width="600" height="200"></canvas>

  <script>
    const labels = {{ top_ports.labels|tojson }};
    const counts = {{ top_ports.counts|tojson }};
    const ctx = document.getElementById('topChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: { labels: labels, datasets: [{ label: 'open count', data: counts }]},
      options: {responsive:true}
    });
  </script>

  <hr>
  <footer class="small text-muted">注意: 許可のないスキャンは違法です。</footer>
</div>
</body>
</html>
"""

HISTORY_HTML = """
<!doctype html>
<html><head><meta charset="utf-8"><title>History</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="p-4">
<div class="container">
  <h3>Scan History</h3>
  <table class="table table-sm">
    <thead><tr><th>id</th><th>scan_time</th><th>address</th><th>ports</th></tr></thead>
    <tbody>
      {% for r in rows %}
        <tr>
          <td>{{ r.id }}</td>
          <td>{{ r.scan_time }}</td>
          <td>{{ r.address }}</td>
          <td>{{ r.port_count }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
  <a href="{{ url_for('index') }}" class="btn btn-secondary">戻る</a>
</div>
</body></html>
"""

@app.route("/")
def index():
    target = TARGETS[0].strip()
    latest = latest_scan_for(DB_CONN, target)
    # compute top ports
    cur = DB_CONN.cursor()
    cur.execute("SELECT port, COUNT(*) as cnt FROM ports WHERE state='open' GROUP BY port ORDER BY cnt DESC LIMIT 15")
    rows = cur.fetchall()
    labels = [r[0] for r in rows]
    counts = [r[1] for r in rows]
    return render_template_string(INDEX_HTML, targets=TARGETS, latest=latest, top_ports={"labels":labels,"counts":counts})

@app.route("/manual-scan", methods=["POST"])
def manual_scan():
    # trigger an immediate scan by spawning a thread that runs one round
    def one_round():
        for t in TARGETS:
            try:
                xml = run_nmap_xml(t)
                parsed = parse_nmap_xml(xml)
                parsed = enrich_ports(parsed)
                alarms = detect_new_ports(DB_CONN, parsed)
                store_results(DB_CONN, parsed)
                if alarms:
                    notify_webhook({"alarms": alarms})
            except Exception as e:
                print("manual scan error:", e)
    threading.Thread(target=one_round, daemon=True).start()
    flash("Manual scan started")
    return redirect(url_for("index"))

@app.route("/history")
def show_history():
    cur = DB_CONN.cursor()
    cur.execute("SELECT id, scan_time, address, (SELECT COUNT(*) FROM ports WHERE host_id=hosts.id) as port_count FROM hosts ORDER BY id DESC LIMIT 200")
    rows = [dict(id=r[0], scan_time=r[1], address=r[2], port_count=r[3]) for r in cur.fetchall()]
    return render_template_string(HISTORY_HTML, rows=rows)

@app.route("/api/latest/<address>")
def api_latest(address):
    return jsonify(latest_scan_for(DB_CONN, address))

# ---------- shutdown handling ----------
import atexit
@atexit.register
def shutdown():
    try:
        scanner.stop()
        scanner.join(timeout=2)
    except Exception:
        pass
    try:
        DB_CONN.close()
    except Exception:
        pass

# ---------- run ----------
if __name__ == "__main__":
    host = os.getenv("PW_BIND", "127.0.0.1")
    port = int(os.getenv("PW_PORT", "5000"))
    app.run(host=host, port=port, debug=False)
