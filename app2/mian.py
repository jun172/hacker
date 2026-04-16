from fastapi import FastAPI
from app2.routers import user
from app2.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Web Development API")

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "FastAPI Web App is running"}