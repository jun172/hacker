from flask import Flask, request, abort, Response
import requests
import re

TARGET = "http://127.0.0.1:5000"

app = Flask(__name__)

RULES = [
    r"(?i)union\s+select",
    r"(?i)or\s+1=1",
    r"(?i)../../",
    r"(?i)<script>",
    r"(?i)cmd=",
]

@app.before_request
def waf_filter():
    payload = request.full_path + request.get_data(as_text=True)

    for rule in RULES:
        if re.search(rule, payload):
            print("[WAF] BLOCK:", request.remote_addr, payload)
            abort(403)

@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","DELETE"])
@app.route("/<path:path>", methods=["GET","POST","PUT","DELETE"])
def proxy(path):
    url = f"{TARGET}/{path}"
    r = requests.request(
        method=request.method,
        url=url,
        headers={k:v for k,v in request.headers if k != "Host"},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
    )
    return Response(r.content, r.status_code, r.headers.items())

if __name__ == "__main__":
    app.run(port=8080)