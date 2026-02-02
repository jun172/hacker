import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts/1') as resp:
            data = await resp.json()
            print(data)
            
asyncio.run(fetch())
