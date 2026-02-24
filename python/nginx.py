from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def root(request: Request):
    return {
        "message": "Hello from Python backend",
        "client_ip": request.client.host 
    }
@app.get("/soc")
async def soc():
    return {"status": "SOC backend alive"}