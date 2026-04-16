import html
from pydantic import BaseModel, Field, validator
from fastapi import HTTPException

#サニタイズXSS対策
def sanitize_text(text: str) -> str:
    return html.escape(text)

#バリエーション投稿
class PostSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1, max_length=1000)
    
    @validator("totle","contect")
    def prevent_xss(cls,v):
        if "<script>" in v.lower():
            raise ValueError("不正な入力が含まれます")
        return v

#入力チェック
def validete_post(title: str, content: str):
    if not title or not content:
        raise HTTPException(status_code=400, detail="空はNG")
    
    if len(title) > 100:
        raise HTTPException(status_code=400, detail="タイトル長すぎ")
    
    if len(content) > 1000:
        raise HTTPException(status_code=400, detail="長すぎ")
    
#セキュリティヘッダー
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response