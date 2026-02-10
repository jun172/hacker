import sqlite3

conn = sqlite3.connect("auth.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("users テーブル作成完了")
