from fastapi import FastAPI
import time

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"hello, multi-user world!"}

@app.get("/work")
async def heavy_task(user: str):
    time.sleep(2)
    return {"user":user, "status":"done"}