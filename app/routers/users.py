from fastapi import APIRouter, Depends, HTTPException
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
        
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    new_user = models.User(username=user.username, password=hashed)
    db.commit()
    return {"msg": "user created"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.Username == user.username).first()
    
    if not db_user or not auth.verift_password(user.password, db_user.passworld):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = auth.create_token({"sub": db_user.username})
    return {"access_token": token}