import asyncio


async def my_async_task():
    await asyncio.sleep(15)
    return 42
