import asyncio
import websockets
import json
from datetime import datetime

PORT = 8765

async def handler(websocket):
    print("✅ クライアント接続")

    try:
        async for message in websocket:
            data = json.loads(message)

            alert = data.get("alert", "不明なアラート")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("====== 🚨 ALERT RECEIVED 🚨 ======")
            print(f"時刻 : {timestamp}")
            print(f"内容 : {alert}")
            print("================================")

    except websockets.exceptions.ConnectionClosed:
        print("❌ クライアント切断")

async def main():
    print(f"🟢 WebSocketサーバ起動 : ws://localhost:{PORT}")
    async with websockets.serve(handler, "localhost", PORT):
        await asyncio.Future()  # 永久待機

asyncio.run(main())