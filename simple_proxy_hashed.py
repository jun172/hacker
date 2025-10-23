#!/usr/bin/env python3
import os
import subprocess
import json
import re
from datetime import datetime
from pathlib import Path
from collections import Counter, defaultdict
from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify, abort

from simple_proxy_hashed import *

# ---------- 設定 ----------
TARGETS = ["192.168.100.83"]   # 監視対象
NMAP_ARGS = "nmap -Pn -sT -p- --min-rate 1000 --open -oG - 192.168.64.10"
BASELINE_DIR = "./baseline"
HISTORY_DIR = "./history"
# --------------------------

os.makedirs(BASELINE_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "replace-this-with-secure-key")

# ----------------- ユーティリティ -----------------
def _sanitize_for_filename(s: str) -> str:
    return re.sub(r'[^0-9A-Za-z._-]', '_', s)

def run_nmap(target, nmap_args, timeout=180):
    cmd = f"nmap {nmap_args} {target} -oG -"
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return proc.stdout, proc.returncode, proc.stderr
    except subprocess.TimeoutExpired:
        return "", -1, "timeout"

def parse_nmap_grepable(out):
    ports = set()
    for line in out.splitlines():
        if line.startswith("Host:"):
            parts = line.split("Ports:")
            if len(parts) < 2: continue
            for pitem in parts[1].strip().split(","):
                if "/open/" in pitem:
                    try:
                        ports.add(int(pitem.split("/")[0]))
                    except:
                        continue
    return sorted(list(ports))

def baseline_path(target):
    return os.path.join(BASELINE_DIR, f"{_sanitize_for_filename(target)}.json")

def load_baseline(target):
    path = baseline_path(target)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f: return json.load(f)
    return {"allowed_ports": []}

def save_baseline(target, data):
    path = baseline_path(target)
    with open(path, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)

def save_history(target, record):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    fname = f"{_sanitize_for_filename(target)}_{ts}.json"
    path = os.path.join(HISTORY_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)

def history_files_for(target):
    files = [f for f in os.listdir(HISTORY_DIR) if f.startswith(_sanitize_for_filename(target) + "_") and f.endswith(".json")]
    files.sort(reverse=True)
    return files

def latest_history_for(target):
    files = history_files_for(target)
    if not files: return None
    with open(os.path.join(HISTORY_DIR, files[0]), "r", encoding="utf-8") as f:
        return json.load(f)

# ----------------- ルート（UI テンプレートは簡素化） -----------------
INDEX_HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>PortWatch Web</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-4">
  <div class="container">
    <h1>PortWatch Web (ローカル)</h1>
    <p>Targets: {{ targets|join(', ') }}</p>

    <div class="mb-3">
      <form action="{{ url_for('scan') }}" method="post" class="d-inline">
        <button class="btn btn-primary">今すぐスキャン</button>
      </form>
      <a class="btn btn-secondary" href="{{ url_for('show_baselines') }}">Baseline</a>
      <a class="btn btn-info" href="{{ url_for('analysis') }}">分析</a>
      <a class="btn btn-dark" href="{{ url_for('proxy_ui') }}">プロキシ</a>
    </div>

    {% if latest %}
      <h4>最新スキャン: {{ latest.timestamp }} ({{ latest.target }})</h4>
      <p>Open ports:
        {% for p in latest.current_ports %}
          {% if p in latest.new_ports %}
            <span class="badge bg-danger">{{ p }}</span>
          {% else %}
            <span class="badge bg-primary">{{ p }}</span>
          {% endif %}
        {% endfor %}
      </p>
      {% if latest.new_ports %}
        <div class="alert alert-danger">New ports: {{ latest.new_ports }}</div>
      {% else %}
        <div class="alert alert-success">No new ports</div>
      {% endif %}
      <h6>Raw nmap (truncated)</h6>
      <pre style="background:#f8f9fa; padding:10px;">{{ latest.raw_nmap[:8000] }}</pre>
    {% else %}
      <div class="alert alert-warning">No scan history yet.</div>
    {% endif %}

    <hr>
    <h5>History files</h5>
    <ul>
      {% for f in histories %}
        <li><a href="{{ url_for('view_history_file', filename=f) }}">{{ f }}</a></li>
      {% endfor %}
    </ul>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    target = TARGETS[0]
    latest = latest_history_for(target)
    histories = history_files_for(target)
    return render_template_string(INDEX_HTML, targets=TARGETS, latest=latest, histories=histories)

@app.route("/scan", methods=["POST"])
def scan():
    if request.remote_addr not in ("127.0.0.1", "::1"):
        abort(403, "Scan allowed from localhost only")
    for target in TARGETS:
        out, code, err = run_nmap(target, NMAP_ARGS, timeout=300)
        ports = parse_nmap_grepable(out)
        baseline = load_baseline(target)
        allowed = set(baseline.get("allowed_ports", []))
        current = set(ports)
        new_ports = sorted(list(current - allowed))
        closed_ports = sorted(list(allowed - current))
        record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "target": target,
            "current_ports": sorted(list(current)),
            "allowed_ports": sorted(list(allowed)),
            "new_ports": new_ports,
            "closed_ports": closed_ports,
            "raw_nmap": out[:200000],
            "nmap_returncode": code,
            "nmap_stderr": err[:10000]
        }
        save_history(target, record)
    flash("Scan finished.")
    return redirect(url_for("index"))

@app.route("/history/<path:filename>")
def view_history_file(filename):
    if ".." in filename or filename.startswith("/"):
        abort(400)
    path = os.path.join(HISTORY_DIR, filename)
    if not os.path.exists(path): abort(404)
    with open(path, "r", encoding="utf-8") as f: data = json.load(f)
    return jsonify(data)

# Baseline pages
BASELINE_HTML = """
<!doctype html><html><head><meta charset="utf-8"><title>Baseline</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="p-4">
<div class="container"><h1>Baseline</h1>
<table class="table table-sm"><thead><tr><th>target</th><th>allowed_ports</th><th>action</th></tr></thead><tbody>
{% for t in targets %}
<tr><td>{{ t }}</td><td>{{ baselines[t].allowed_ports }}</td>
<td>
<form action="{{ url_for('init_baseline') }}" method="post" style="display:inline">
<input type="hidden" name="target" value="{{ t }}">
<button class="btn btn-warning btn-sm">Init</button>
</form>
</td></tr>
{% endfor %}
</tbody></table><a href="{{ url_for('index') }}">Back</a></div></body></html>
"""

@app.route("/baselines")
def show_baselines():
    baselines = {t: load_baseline(t) for t in TARGETS}
    return render_template_string(BASELINE_HTML, targets=TARGETS, baselines=baselines)

@app.route("/baselines/init", methods=["POST"])
def init_baseline():
    if request.remote_addr not in ("127.0.0.1", "::1"):
        abort(403)
    target = request.form.get("target")
    if target not in TARGETS: abort(400)
    out, code, err = run_nmap(target, NMAP_ARGS, timeout=180)
    ports = parse_nmap_grepable(out)
    save_baseline(target, {"allowed_ports": sorted(ports), "initialized": datetime.utcnow().isoformat()+"Z"})
    flash(f"Baseline set for {target}")
    return redirect(url_for("show_baselines"))

# ----------------- 分析 -----------------
ANALYSIS_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8"><title>Analysis</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-4">
<div class="container">
<h1>Port Analysis</h1>
<p>Top ports (total occurrences across history)</p>
<canvas id="barChart"></canvas>
<hr>
<p>Time series for top ports</p>
<canvas id="lineChart" height="150"></canvas>
<a class="btn btn-secondary" href="{{ url_for('index') }}">Back</a>
</div>

<script>
const labels = {{ ts_labels|tojson }};
const bar_labels = {{ bar_labels|tojson }};
const bar_counts = {{ bar_counts|tojson }};
const series = {{ series|tojson }};
const series_ports = {{ series_ports|tojson }};

// Bar chart
new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: { labels: bar_labels, datasets: [{ label: 'occurrences', data: bar_counts }]},
  options: { responsive: true }
});

// Line chart (time series)
const datasets = series_ports.map((port, idx) => ({
  label: String(port),
  data: series[idx],
  fill: false,
  tension: 0.2
}));
new Chart(document.getElementById('lineChart'), {
  type: 'line',
  data: { labels: labels, datasets: datasets },
  options: { responsive: true, scales: { x: { display: true } } }
});
</script>
</body>
</html>
"""

def analyze_history_time_series(target, top_n=6):
    # 読み込む履歴ファイル（古→新）
    files = sorted(history_files_for(target))
    if not files:
        return [], [], [], []
    # collect timestamps and port lists
    timestamps = []
    per_file_ports = []
    for fn in files:
        with open(os.path.join(HISTORY_DIR, fn), "r", encoding="utf-8") as f:
            j = json.load(f)
            timestamps.append(j.get("timestamp", fn.split("_")[-1].replace(".json","")))
            per_file_ports.append(j.get("current_ports", []))
    # flatten counts to pick top ports
    all_ports = Counter([p for ports in per_file_ports for p in ports])
    top = [p for p,c in all_ports.most_common(top_n)]
    # build series: for each top port, count presence per timestamp (0/1) or count (presence->1)
    series = []
    for port in top:
        series.append([1 if port in ports else 0 for ports in per_file_ports])
    return timestamps, top, series, all_ports.most_common()

@app.route("/analysis")
def analysis():
    target = TARGETS[0]
    ts_labels, series_ports, series_data, all_counts = analyze_history_time_series(target, top_n=6)
    # prepare bar chart data (top 10)
    bar = all_counts[:10]
    bar_labels = [p for p,c in bar]
    bar_counts = [c for p,c in bar]
    return render_template_string(ANALYSIS_HTML,
                                  ts_labels=ts_labels,
                                  bar_labels=bar_labels,
                                  bar_counts=bar_counts,
                                  series=series_data,
                                  series_ports=series_ports)

# ----------------- プロキシ UI -----------------
PROXY_UI_HTML = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Proxy UI</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="p-4">
<div class="container">
<h1>Proxy UI</h1>
<p>ローカルのみ使用。URL にフルパス（例: http://192.168.100.83:8000/path）を入れて送信してください。</p>
<form id="proxyForm" action="{{ url_for('proxy_fetch') }}" method="get" target="proxyFrame">
  <div class="mb-3">
    <input name="url" class="form-control" placeholder="http://..." />
  </div>
  <button class="btn btn-primary">Fetch via proxy</button>
</form>
<hr>
<iframe name="proxyFrame" style="width:100%; height:600px; border:1px solid #ddd;"></iframe>
<a class="btn btn-secondary" href="{{ url_for('index') }}">Back</a>
</div>
</body>
</html>
"""

@app.route("/proxy_ui")
def proxy_ui():
    return render_template_string(PROXY_UI_HTML)

@app.route("/proxy_fetch")
def proxy_fetch():
    # ローカルからのみ
    if request.remote_addr not in ("127.0.0.1", "::1"):
        abort(403)
    url = request.args.get("url", "")
    if not url:
        abort(400, "url required")
    # call simple proxy
    return TARGETS(url)

# ----------------- 起動 -----------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2000, debug=True)
