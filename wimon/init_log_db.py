import sqlite3

conn = sqlite3.connect("attack_logs.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS attack_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    ip TEXT,
    attempts INTEGER,
    success INTEGER,
    elapsed REAL,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("attack_logs.db 初期化完了")
