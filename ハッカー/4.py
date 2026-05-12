from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def ping():
    ip = request.args.get("ip", "")
    
    # ❌ 超危険な実装（意図的に脆弱）
    command = "ping -c 1 " + ip
    result = os.popen(command).read()

    return "<pre>" + result + "</pre>"

app.run(host="0.0.0.0", port=5000)
