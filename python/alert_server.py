import asyncio
import websockets
import json
from datetime import datetime

async def handler(ws):
    async for message in ws:
        data = json.loads(message)
        print(f"[{datetime.now()}] 🚨 ALERT: {data['alert']}")
        
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("🚨 Alert Server 起動")
        await asyncio.Future()
        
asyncio.run(main())