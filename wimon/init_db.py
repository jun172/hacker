import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

# テーブル作成
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# テストデータ投入
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "pass1"))
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "pass2"))

conn.commit()
conn.close()

print("users.db 作成完了")
