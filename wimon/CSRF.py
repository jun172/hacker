from flask import Blueprint, render_template, request, session, redirect
from datetime import datetime

CSRF = Blueprint('CSRF', __name__, template_folder='templates')

balance = 100000
history = []  # 取引履歴リスト

# ─────────────────────────────
# ログインページ
# ─────────────────────────────
@CSRF.route('/CSRF.html', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["logged_in"] = True
        return redirect("/CSRF/bank.html")
    return render_template("CSRF.html")

# ─────────────────────────────
# 銀行ページ（脆弱版）
# ─────────────────────────────
@CSRF.route('/bank.html', methods=["GET", "POST"])
def bank():
    global balance, history

    if not session.get("logged_in"):
        return redirect("/CSRF/CSRF.html")

    message = ""

    if request.method == "POST":
        # CSRFチェックなし
        amount = int(request.form.get("amount", 0))
        balance -= amount
        message = f"{amount}円送金しました！（脆弱）"

        # 取引履歴に追加
        history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount
        })

    return render_template(
        "bank.html",
        balance=balance,
        message=message,
        history=history
    )

# ─────────────────────────────
# 攻撃ページ
# ─────────────────────────────
@CSRF.route('/attack')
def attack():
    return render_template("attack.html")