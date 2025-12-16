from flask import Blueprint, render_template

DARK = Blueprint('DARK', __name__, template_folder='templates')

@DARK.route("/")  # <- ここが重要
def market():
    return render_template("market.html")