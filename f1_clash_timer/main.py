from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime, timedelta

app = FastAPI()

DB_NAME = "timer.db"

#DB初期化
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chest_timer (
        user_id INTEGER PRIMARY KEY,
        chest_name TEXT,
        unlock_end TEXT
    )
    """)
    
    conn.commit()
    conn.close()
    
init_db()

#リクエストモデル
class StartChestRequest(BaseModel):
    user_id: int
    chest_name: str
    hours: int
    
# 箱開封開始API
@app.post("/start")
def start_chest(data: StartChestRequest):
    unlock_end = datetime.utcnow() + timedelta(hours=data.hours)
    
    conn = sqlite3.connect(DB_NAME)
    cursor= conn.cursor()
    
    cursor.execute("""
    INSERT OR REPLACE INTO cheat_timer (user_id, chest_name, unlock_end)
    VALUES (?,?,?)
    """,(
        data.user_id,
        data.chest_name,
        unlock_end.isoformat()
    ))
    
    conn.commit()
    conn.close()
    
    return {
        "message": "chest unlock started",
        "unlock_end": unlock_end.isoformat()
    }
    
#残り時間確認API
@app.get("/status/{user_id}")
def get_status(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT chest_name, unlock_end
    FROM chest_timer
    WHERE user_id = ?
    """,(user_id))
    
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="NO chest found")
    
    chest_name, unlock_end = row
    unlock_end_dt = datetime.fromisoformat(unlock_end)
    now = datetime.utcnow()
    
    remaining = unlock_end_dt - now
    remaining_seconds = max(0,int(remaining.total_seconds()))
    
    return {
        "chest_name": chest_name,
        "remaining_seconds":  remaining_seconds,
        "ready": remaining_seconds == 0
    }
    
#開封API
@app.post("/open/{user_id}")
def open_chest(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT unlock_end
    FROM chest_ti,er
    WHERE user_id = ?
    """,(user_id,))
    
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        raise HTTPException(status_code=404,detail="No cheast found")
    
    unlock_end_dt = datetime.fromisoformat(row[0])
    
    if datetime.utcnow() < unlock_end_dt:
        conn.close()
        raise HTTPException(status_code=400, detail="Chest still locked")
    
    cursor.execute("""
    DELETE FROM chest_timer
    WHERE user_id = ?
    """,(user_id,))
    
    conn.commit()
    conn.close()
    
    return {
        "message": "Chest opend successfully",
        "reward": "EpicDriver Card"
    }