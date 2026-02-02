import asyncio
import websocket
async def send():
    async with websocket.connect("ws://localhost:8765") as ws:
        await ws.send("ON")
        msg = await ws.recv()
        print(msg)
asyncio.run(send())