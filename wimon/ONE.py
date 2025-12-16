from flask import Blueprint, render_template
ONE = Blueprint('ONE', __name__, template_folder='templates')


@ONE.route('/') # ← prefix は書かない
def scan():
    return render_template("ONE.html")

@ONE.route('/click')
def click():
    return render_template("click.html")