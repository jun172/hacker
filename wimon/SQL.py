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
        (2, 'user', 'password'),
        (3,'神戸電子','kobedensi')
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
    all_users = []          # ← 追加（DB全体）
    show_result = False
    result_message = ""
    debug_query = ""

    try:
        conn = get_db()
        cur = conn.cursor()

        # 🔥 常にDBの中身を取得（教材用）
        cur.execute("SELECT * FROM users")
        all_users = cur.fetchall()

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

            cur.execute(debug_query)
            db_result = cur.fetchall()

            if db_result:
                result_message = "⚠️ ログイン成功（SQLインジェクションの可能性あり）"
            else:
                result_message = "ログイン失敗"

            show_result = True

    except Exception as e:
        result_message = f"SQLエラー: {e}"
        show_result = True

    finally:
        conn.close()

    return render_template(
        "SQL.html",
        show_result=show_result,
        result_message=result_message,
        query=debug_query,
        db_result=db_result,
        all_users=all_users     # ← HTMLに渡す
    )


@SQL.route("/SQL2.html",methods=["GET"])
def sql2():
    conn = get_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    conn.close()
    
    return render_template("/SQL2.html",users=users)

@SQL.route("/SQL3.html",methods=["GET"])
def sql3():
    conn = get_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    conn.close()
    
    return render_template("/SQL3.html",users=users)

@SQL.route("/SQL4.html",methods=["GET","POST"])
def sql4():
    conn = get_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    conn.close()
    
    return render_template("/SQL4.html",users=users)