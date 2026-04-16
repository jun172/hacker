from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas, auth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str= Header(...), db: Session= Depends(get_db)):
    payload = auth.verify_token(token)
    username = payload.get("sub")
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

@router.post("/posts")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    new_post = models.Post(title = post.title, content = post.content, user_id = user.id)
    db.add(new_post)
    db.commit()
    return {"msg": "post created"}

@router.get("/posts")
def get_post(db: Session=Depends(get_db)):
    return db.query(models.Post).all()

@router.put("/posts/{post_id}")
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    
    if db_post.user_id != user.id:
        raise HTTPException(status_code=403)
    
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    return {"msg":"updated"}

@router.delete("/posts/{post_id}")
def dalete_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    
    if db_post.user_id != user.id:
        raise HTTPException(status_code=403)
    
    db.delete(db_post)
    db.commit()
    return {"msg":"deleted"}