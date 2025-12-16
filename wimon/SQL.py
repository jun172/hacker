from flask import Blueprint, render_template, request
import logging
import sqlite3
import os

logging.basicConfig(level=logging.DEBUG)

SQL = Blueprint("SQL", __name__, template_folder="templates")

# 🔴 DBの場所を固定（超重要）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # テーブル作成
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # 初期データ
    cur.execute("""
    INSERT OR IGNORE INTO users (id, username, password)
    VALUES
        (1, 'admin', 'admin'),
        (2, 'user', 'password')
    """)

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# 🔥 起動時に必ずDBを用意
init_db()


@SQL.route("/login", methods=["GET", "POST"])
def login():
    db_result = []
    show_result = False
    result_message = ""
    debug_query = ""

    if request.method == "POST":
        user = request.form["username"]
        pwd  = request.form["password"]

        # ❌ わざと脆弱（SQLインジェクション教材用）
        debug_query = f"""
        SELECT * FROM users
        WHERE username = '{user}'
        AND password = '{pwd}'
        """

        logging.debug(f"DEBUG SQL: {debug_query}")

        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute(debug_query)
            db_result = cur.fetchall()

            if db_result:
                result_message = "⚠️ ログイン成功（SQLインジェクションの可能性あり）"
            else:
                result_message = "ログイン失敗"

        except Exception as e:
            result_message = f"SQLエラー: {e}"

        finally:
            conn.close()

        show_result = True

    return render_template(
        "SQL.html",
        show_result=show_result,
        result_message=result_message,
        query=debug_query,
        db_result=db_result
    )