import aiohttp, asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com") as r:
            print(await r.text())
asyncio.run(fetch())