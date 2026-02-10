import asyncio
import psutil
import subprocess
import json
import time
import websockets

WS_URL = "ws://localhost:8765"
TRAFFIC_LIMIT = 10 * 1024 * 1024
TARGET_HOST = "8.8.8.8"

async def send_alert(msg):
    async with websockets.connect(WS_URL) as ws:
        await ws.send(json.dumps({"alert": msg}))
        
def ping_check():
    return subprocess.run(
        ["ping", "-c","1",TARGET_HOST],
        stdout=subprocess.DEVNULL
    ).returncode == 0
    
def get_traffic():
    net = psutil.net_io_counters()
    return net.bytes_sent + net.bytes_recv

def nmap_scan():
    out = subprocess.check_output(
        ["nmap","-p","22,23,3389","localhost"]
    ).decode()
    return "open" in out

def bloock_traffic():
    subprocess.run(["iptables","-A","OUTPUT","-j","DROP"])
    
async def monitor():
    prev = get_traffic()
    
    while True:
        await asyncio.sleep(5)
        now = get_traffic()
        diff = now - prev
        prev = now
        
        if diff > TRAFFIC_LIMIT:
            await send_alert("通信量異常 → 自動遮断")
            bloock_traffic()
            break
        
        if nmap_scan():
            await send_alert("危険ポート検出 → 遮断")
            bloock_traffic()
            break

async def main():
    if not ping_check():
        await send_alert("ネットワーク疎通不可")
        return 
    await monitor()
    
asyncio.run(main())