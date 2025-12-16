from flask import Blueprint, render_template, request
import os

DT = Blueprint('DT', __name__, template_folder='templates')

BASE_DIR = os.path.abspath("files")

@DT.route("/")
def index():
    return render_template("DT.html")

@DT.route("/read")
def read_file():
    file = request.args.get("file","")
    safe_path = os.path.abspath(os.path.join(BASE_DIR,file))

    if not safe_path.startswith(BASE_DIR):
        return "⚠️ ディレクトリ外は禁止！"

    if not os.path.exists(safe_path):
        return "❌ ファイルが存在しない！"

    with open(safe_path,"r",encoding="utf-8") as f:
        return f.read()

