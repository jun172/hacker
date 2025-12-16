from flask import Blueprint, render_template, request, make_response

XSS = Blueprint('XSS', __name__, template_folder='templates')

@XSS.route("/", methods=["GET", "POST"])
def xss_home():
    message = ""

    if request.method == "POST":
        comment = request.form.get("comment", "")
        message = comment  # XSS用（危険）

    resp = make_response(render_template("xss.html", message=message))

    # ★教材用：HttpOnly を付けない
    resp.set_cookie("sessionid", "ABC123")

    return resp
