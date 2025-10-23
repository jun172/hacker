#!/usr/bin/env python3
import os
import subprocess
import json
from datetime import datetime
from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify, abort
from urllib.parse import urlparse
from simple_proxy_hashed import * # あなたの既存モジュール

# ---------- 設定 ----------
TARGETS = ["http://192.168.100.83"]
NMAP_ARGS = "-sT -p- --min-rate 1000 --open"
BASELINE_DIR = "./baseline"
HISTORY_DIR = "./history"
# --------------------------

os.makedirs(BASELINE_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "replace-this-with-secure-key")

# ----------------- ユーティリティ -----------------
def _sanitize_for_filename(s: str) -> str:
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in s)

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
                    except: continue
    return sorted(list(ports))

def load_baseline(target):
    path = os.path.join(BASELINE_DIR, f"{_sanitize_for_filename(target)}.json")
    if os.path.exists(path):
        with open(path, "r") as f: return json.load(f)
    return {"allowed_ports": []}

def save_baseline(target, data):
    path = os.path.join(BASELINE_DIR, f"{_sanitize_for_filename(target)}.json")
    with open(path, "w") as f: json.dump(data, f, indent=2)

def save_history(target, record):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    fname = f"{_sanitize_for_filename(target)}_{ts}.json"
    path = os.path.join(HISTORY_DIR, fname)
    with open(path, "w") as f: json.dump(record, f, indent=2)

def latest_history_for(target):
    files = [f for f in os.listdir(HISTORY_DIR) if f.startswith(_sanitize_for_filename(target) + "_") and f.endswith(".json")]
    if not files: return None
    files.sort(reverse=True)
    with open(os.path.join(HISTORY_DIR, files[0]), "r") as f: return json.load(f)

def analyze_ports(target):
    """ 履歴 JSON からポート分布を集計 """
    from collections import Counter
    files = [f for f in os.listdir(HISTORY_DIR) if f.startswith(_sanitize_for_filename(target) + "_") and f.endswith(".json")]
    ports_all = []
    for f in files:
        data = json.load(open(os.path.join(HISTORY_DIR, f), "r"))
        ports_all.extend(data.get("current_ports", []))
    counter = Counter(ports_all)
    return counter.most_common()

# ----------------- ルーティング -----------------
@app.route("/")
def index():
    target = TARGETS[0]
    latest = latest_history_for(target)
    histories = sorted([f for f in os.listdir(HISTORY_DIR) if f.startswith(_sanitize_for_filename(target) + "_") and f.endswith(".json")], reverse=True)
    return render_template_string("""
<!doctype html>
<html>
<head>
<meta charset="utf-8"><title>PortWatch Web</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<h1>PortWatch Web</h1>
<form action="{{ url_for('scan') }}" method="post"><button>Scan</button></form>
<a href="{{ url_for('analysis') }}">分析を見る</a>
{% if latest %}
<p>最新スキャン: {{ latest.timestamp }}</p>
<p>オープンポート: {{ latest.current_ports }}</p>
{% endif %}
<h3>履歴</h3>
<ul>{% for h in histories %}<li><a href="{{ url_for('view_history_file', filename=h) }}">{{ h }}</a></li>{% endfor %}</ul>
</body>
</html>
""", latest=latest, histories=histories)

@app.route("/scan", methods=["POST"])
def scan():
    if request.remote_addr not in ("127.0.0.1", "::1"): abort(403)
    for target in TARGETS:
        out, code, err = run_nmap(target, NMAP_ARGS, timeout=300)
        ports = parse_nmap_grepable(out)
        baseline = load_baseline(target)
        allowed = set(baseline.get("allowed_ports", []))
        current = set(ports)
        new_ports = sorted(list(current - allowed))
        closed_ports = sorted(list(allowed - current))
        record = {"timestamp": datetime.utcnow().isoformat()+"Z","target":target,
                  "current_ports": sorted(list(current)),"allowed_ports":sorted(list(allowed)),
                  "new_ports":new_ports,"closed_ports":closed_ports,"raw_nmap":out[:200000],
                  "nmap_returncode":code,"nmap_stderr":err[:10000]}
        save_history(target, record)
    flash("Scan finished")
    return redirect(url_for("index"))

@app.route("/history/<path:filename>")
def view_history_file(filename):
    if ".." in filename or filename.startswith("/"): abort(400)
    path = os.path.join(HISTORY_DIR, filename)
    if not os.path.exists(path): abort(404)
    with open(path,"r") as f: data=json.load(f)
    return jsonify(data)

@app.route("/baselines/init", methods=["POST"])
def init_baseline():
    if request.remote_addr not in ("127.0.0.1","::1"): abort(403)
    target = request.form.get("target")
    out, code, err = run_nmap(target, NMAP_ARGS, timeout=180)
    ports = parse_nmap_grepable(out)
    save_baseline(target, {"allowed_ports": sorted(ports), "initialized": datetime.utcnow().isoformat()+"Z"})
    flash(f"Baseline for {target} initialized")
    return redirect(url_for("index"))

# ----------------- 分析ルート -----------------
@app.route("/analysis")
def analysis():
    target = TARGETS[0]
    data = analyze_ports(target)
    labels = [str(p) for p, c in data]
    counts = [c for p, c in data]
    return render_template_string("""
<h1>ポート分布分析</h1>
<canvas id="chart"></canvas>
<script>
var ctx = document.getElementById('chart').getContext('2d');
new Chart(ctx,{type:'bar',data:{labels:{{ labels|tojson }},datasets:[{label:'出現回数',data:{{ counts|tojson }},backgroundColor:'rgba(54,162,235,0.5)'}]}});
</script>
""", labels=labels, counts=counts)

# ----------------- プロキシルート -----------------
@app.route("/proxy/<path:url>")
def proxy(url):
    # localhost からのみ
    if request.remote_addr not in ("127.0.0.1","::1"): abort(403)
    return TARGETS (url)

# ----------------- 起動 -----------------
if __name__=="__main__":
    app.run(host="127.0.0.1", port=2000, debug=True)
