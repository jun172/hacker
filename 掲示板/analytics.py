import sqlite3
DATABESE = "database.db"

def get_stats():
    conn = sqlite3.connect(DATABESE)
    
    total_logins = conn.execute("""
        SELECT COUNT(*) FROM session_logs
        WHERE action = 'login
    """).fetchone()[0]
    
    