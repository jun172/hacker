from flask import Flask, render_template, request,redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                time TEXT NOT NULL
            )
        """)
    conn.commit()
    conn.close()
    
@app.route("/",method=["GET","POST"])
def index():
    if request.method=="POST":
        name = request.form["name"] #名前を使い
        action = request.form["action"]#出勤
        time = datetime.now().strptime("%Y-%m-%d %H:%M:%S")#時間　入室時間
        
        conn = sqlite3.connect("attendance.db") #データベース接続
        c = conn.cursor()
        c.execute(
            "INSERT INTO attendance (employee_name, action, time) VALUES (?,?,?,)",
            (name, action, time)
        )
        conn.commit()
        conn.close()
        
        return redirect("/")
    
    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)