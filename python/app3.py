from fastapi import FastAPI
import threading
import time
from detector import analye_log

app = FastAPI()

SOC_STATUS = {
    "running":True,
    "alerts":[]
}

def soc_loop():
    """SOC 常駐監視ループ"""
    while SOC_STATUS["running"]:
        alert =  analye_log()
        if alert:
            SOC_STATUS["alerts"].append(alert)
            print("[ALERT]",alert)
        time.sleep(3)
        
@app.on_event("startup")
def startup_event():
    thred = threading.Thread(target=soc_loop, daemon=True)
    thred.start()
    
@app.get("/")
def status():
    return {
        "soc":"running",
        "alerts":SOC_STATUS["alerts"][-10:]
    }