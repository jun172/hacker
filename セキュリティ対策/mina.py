from fastapi import FastAPI, Response
import sqlite3

from security import PostSchema, sanitize_text, add_security_headers

app = FastAPI()

conn = sqlite3.connect("blog.db", check_same_thread=False)
cursor = conn.cursor()

@app.post("/post")
def create_post(post: PostSchema, responce: Response):
    #サニタイズ
    title = sanitize_text(post.title)
    content = sanitize_text(post.content)
    
    #SQLインジェクション対策(プレースホルダ)
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (?,?)",
        (title, content)
    )
    conn.commit()
    
    return add_security_headers({"message": "投稿完了"})