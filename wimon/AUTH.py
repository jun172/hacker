from flask import Blueprint, render_template, request
import sqlite3
import time
import itertools
import string
from datetime import datetime

AUTH = Blueprint("AUTH", __name__, template_folder="templates")

USER_DB = "auth.db"
LOG_DB = "attack_logs.db"

# ===============================
# 🔑 パスワード生成
# ===============================
def brute_passwords(max_len):
    chars = string.ascii_letters + string.digits
    for length in range(1, max_len + 1):
        for combo in itertools.product(chars, repeat=length):
            yield "".join(combo)

# ===============================
# 📝 新規登録
# ===============================
@AUTH.route("/", methods=["GET", "POST"])
def register():
    msg = ""

    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        try:
            conn = sqlite3.connect(USER_DB)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (u, p)
            )
            conn.commit()
            msg = "登録成功"
        except sqlite3.IntegrityError:
            msg = "そのIDは既に存在します"
        finally:
            conn.close()

    return render_template("register.html", msg=msg)

# ===============================
# 🔑 通常ログイン
# ===============================
@AUTH.route("/login", methods=["GET", "POST"])
def login():
    msg = ""

    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(USER_DB)
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM users WHERE username=? AND password=?",
            (u, p)
        )
        user = cur.fetchone()
        conn.close()

        msg = "ログイン成功" if user else "ID または パスワードが違います"

    return render_template("login.html", msg=msg)

# ===============================
# 💣 ブルートフォース攻撃
# ===============================
@AUTH.route("/brute", methods=["GET", "POST"])
def brute():
    result = None
    log_lines = []

    if request.method == "POST":
        username = request.form["username"]
        max_len = int(request.form["max_len"])
        ip = request.remote_addr

        attempts = 0
        found = None
        start = time.time()

        conn = sqlite3.connect(USER_DB)
        cur = conn.cursor()

        for p in brute_passwords(max_len):
            attempts += 1
            time.sleep(0.03)

            cur.execute(
                "SELECT id FROM users WHERE username=? AND password=?",
                (username, p)
            )

            if cur.fetchone():
                found = p
                log_lines.append(f"[+] SUCCESS {username} / {p}")
                break

            if attempts % 500 == 0:
                log_lines.append(f"[-] 試行 {attempts} 回")

        conn.close()
        elapsed = round(time.time() - start, 2)

        # ログ保存
        conn = sqlite3.connect(LOG_DB)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO attack_logs
            (username, ip, attempts, success, elapsed, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            username,
            ip,
            attempts,
            1 if found else 0,
            elapsed,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        conn.commit()
        conn.close()

        result = {
            "attempts": attempts,
            "found": found,
            "elapsed": elapsed,
            "ip": ip
        }

    return render_template("brute.html", result=result, log=log_lines)

# ===============================
# 📊 攻撃ログ表示
# ===============================
@AUTH.route("/logs")
def logs():
    conn = sqlite3.connect(LOG_DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT id, username, ip, attempts, success, elapsed, created_at
        FROM attack_logs
        ORDER BY id DESC
    """)
    rows = cur.fetchall()
    conn.close()

    return render_template("logs.html", rows=rows)
