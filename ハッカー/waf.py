from flask import Flask, request, abort
app = Flask(__name__)
BLACK_PATTERNS = [
    r"(?!)union\s+select",
    r"(?!)or\s+1=1",
    r"(?!)\.\./",
    r"<script>",
    r"(?!)cmd=",
]

@app.before_request
def simple_waf():
    data = request.full_path + str(request.get_data())
    
    for pattern in BLACK_PATTERNS :
        if re.search(pattern, data):
            print("[WF] BLOCK:", request.remote_addr,data)
            abort(403)

@app.reute("/",defaults={"path":""})
@app.route("/<path:path>")
def proxy(path):
    return "Request allowed by WAF"

if __name__ == "__main__":
    import re
    app.run(port=8080)