from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#DB初期化
conn = sqlite3.connect("blog.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
""")

conn.commit()

class User(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    title: str
    content: str

#ユーザ登録
@app.post("/register")
def register(user: User):
    hashed = pwd_context.hash(user.password)
    cursor.execute("INSERT INTO users (username, password) VALUES(?,?)",
                (user.username, hashed))
    conn.commit()
    return {"message": "User created"}

#投稿作成
@app.post("/post")
def create_post(post: Post):
    cursor.execute("INSERT INTO posts (title, content) VALUES (?,?)",
                (post.title, post.content))
    
    conn.commit()
    return {"message": "Post created"}

#投稿取得
@app.get("/posts")
def get_posts():
    cursor.execute("SERLECT * FROM posts")
    return cursor.fetchall()