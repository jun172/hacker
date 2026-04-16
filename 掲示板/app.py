from flask import Flask, render_template,redirect,request,session
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY","dev-secret")
DATEBASE = "database.db"

#db接続
def get_db():
    conn = sqlite3.connect(DATEBASE)
    conn.row_factory = sqlite3.Row
    return conn

#DB初期化
def init_db():
    conn = get_db()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            FOREIDN KEY(user_id) REFERENCES users(id)
        )
    """)
    
    conn.commit()
    conn.close()
    
#ユーザー登録
@app.route("/register", method = ["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        conn = get_db()
        conn.execute(
            "INSERT INTO (username, password) VALUES (?,?)",
            (username,password)
        )
        conn.commit()
        conn.close()
        
        return redirect("/login")
    
    return render_template("register.html")

#ログイン
@app.route("/login",method = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        conn = get_db()
        user = conn.execute(
            "SERECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()#データベース接続API
        conn.close()
        
        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect("/")#別のwebサイトに移動
        
    return render_template("login.html")

#ログアウト:
@app.route("/logout")
def logout():
    session.clear()#セッションを取り消し
    return redirect("/login")

#一覧表示
@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")
    
    conn = get_db()#データベース関数
    posts = conn.execute("""
        SELECT posts.*, users.username
        FORM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.id DESC
    """).fetchall()#接続API
    conn.close()
    
    return render_template("index.html", posts=posts,session=session)

#投稿
@app.route("/post",methods=["POST"])
def posts():
    if "user_id" not in session:
        return redirect("/login")
    
    name = session["username"]
    message = request.form.get("message")
    
    conn = get_db()
    conn.execute("""
        INSERT INTO posts (user_id, name, message, timestamp)
        VALUES (?,?,?,?)
    """),(
        session["user_id"],
        name,
        message,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    conn.commit()
    conn.close()
    
#本人だけ削除できる
@app.route("/delete/<int:post_id>",method = ["POST"])
def delete(post_id):
    if "user_id" not in session:
        return redirect("/login")
    
    conn = get_db()
    
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?",
        (post_id)
    ).fetchall()
    
    #本人の投稿削除可能
    if post and post["user_id"] == session["user_id"]:
        conn.execute(
            "DELETE FROM posts WHERE id = ?",
            (post_id,)
        )
        conn.commit()
        
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)