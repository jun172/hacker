from flask import Blueprint, render_template, request
import os

DT = Blueprint('DT', __name__, template_folder='templates')

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "files")
)

@DT.route("/")
def index():
    return render_template("DT.html")

@DT.route("/read")
def read_file():
    file = request.args.get("file", "")

    # ❌ 脆弱：.txt が無ければ付与（Traversal 可）
    if not file.endswith(".txt"):
        file = file + ".txt"

    target_path = os.path.join(BASE_DIR, file)

    if not os.path.exists(target_path):
        return "❌ ファイルが存在しない！"

    # 🔓 完全脆弱版：そのまま開く
    with open(target_path, "r", encoding="utf-8") as f:
        return f.read()
