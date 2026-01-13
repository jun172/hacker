from flask import Flask, request, render_template_string, redirect, url_for
import requests
import socket, ssl
from urllib.parse import urlparse
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>簡易脆弱性パッシブチェック</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-4">
  <div class="container">
    <h1>簡易脆弱性パッシブチェック</h1>
    <form method="post" class="mb-3">
      <div class="input-group">
        <input name="target" class="form-control" placeholder="https://example.com" required>
        <button class="btn btn-primary">チェック</button>
      </div>
    </form>

    {% if result %}
      <h2>結果: {{ result.url }}</h2>

      <h3>HTTP ヘッダ</h3>
      <table class="table table-sm">
        <thead><tr><th>Header</th><th>Value</th></tr></thead>
        <tbody>
        {% for k,v in result.headers.items() %}
          <tr><td>{{k}}</td><td>{{v}}</td></tr>
        {% endfor %}
        </tbody>
      </table>

      <h3>セキュリティチェック</h3>
      <ul>
        <li>X-Frame-Options: {{ 'OK' if result.headers.get('X-Frame-Options') else 'Missing' }}</li>
        <li>Content-Security-Policy: {{ 'OK' if result.headers.get('Content-Security-Policy') else 'Missing' }}</li>
        <li>X-Content-Type-Options: {{ 'OK' if result.headers.get('X-Content-Type-Options') else 'Missing' }}</li>
        <li>Strict-Transport-Security: {{ 'OK' if result.headers.get('Strict-Transport-Security') else 'Missing' }}</li>
        <li>Set-Cookie HttpOnly/Secure: {{ 'Check cookies' }}</li>
      </ul>

      <h3>robots.txt</h3>
      <pre>{{ result.robots or 'Not found' }}</pre>

      <h3>TLS 証明書</h3>
      {% if result.cert %}
        <p>Subject: {{ result.cert.subject }}</p>
        <p>Issuer: {{ result.cert.issuer }}</p>
        <p>有効期限 (notAfter): {{ result.cert.notAfter }} （UTC）</p>
      {% else %}
        <p>非HTTPS または 証明書取得失敗</p>
      {% endif %}
    {% endif %}
  </div>
</body>
</html>
"""

def fetch_headers(target):
    try:
        resp = requests.get(target, timeout=8, allow_redirects=True)
        headers = {k: v for k, v in resp.headers.items()}
        return headers, resp
    except Exception as e:
        return {}, None

def fetch_robots(target):
    try:
        parsed = urlparse(target)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        r = requests.get(robots_url, timeout=5)
        if r.status_code == 200:
            return r.text
        return None
    except:
        return None

def get_cert_info(hostname, port=443):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                # Extract subject and issuer summary
                subject = dict(x[0] for x in cert.get('subject', ()))
                issuer = dict(x[0] for x in cert.get('issuer', ()))
                notAfter = cert.get('notAfter')
                return {
                    "subject": subject,
                    "issuer": issuer,
                    "notAfter": notAfter
                }
    except Exception:
        return None

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        target = request.form["target"].strip()
        # Basic validation: require http or https
        if not (target.startswith("http://") or target.startswith("https://")):
            target = "http://" + target
        headers, resp = fetch_headers(target)
        robots = fetch_robots(target)
        parsed = urlparse(target)
        cert = None
        if parsed.scheme == "https":
            cert = get_cert_info(parsed.netloc.split(':')[0], port=443)
        result = type("R", (), {})()
        result.url = target
        result.headers = headers
        result.robots = robots
        result.cert = cert
        return render_template_string(HTML_TEMPLATE, result=result)
    return render_template_string(HTML_TEMPLATE, result=None)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
