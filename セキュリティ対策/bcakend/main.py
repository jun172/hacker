from fastapi import FastAPI, Depends
import sqlite3

from auth import hash_password, verify_password, get_current_user,create_access_token
from pydantic import BaseModel

app = FastAPI()

conn = sqlite3.connect("blog.db",check_same_thread=False)
cursor = conn.cursor()

#テーブル
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

class User(BaseModel):
    username: str
    password: str
    
#登録
@app.post("/register")
def register(user: User):
    hashed = hash_password(user.password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?,?)",
            (user.username,hashed)
        )
        conn.commit()
        return {"message": "登録成功"}
    except:
        return {"error": "ユーザ存在"}
    
#ログイン
@app.post("/login")
def login(user: User):
    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (user.username)
    )
    result = cursor.fetchone()
    
    if not result:
        return {"error":"ユーザーなし"}
    
    hashed_password = result[0]
    
    if not verify_password(user.password, hashed_password):
        return {"error": "パスワードが違う"}
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token}

#認証必須API
@app.get("/protected")
def protected(user: str = Depends(get_current_user)):
    return {"message":f"{user}さんログイン中"}