import asyncio
async def task(name):
    await asyncio.sleep(1)
    print(f"{name} 完了")

asyncio.run(task("Task1"))