import asyncio
from typing import Any
from asyncio.tasks import FIRST_COMPLETED


async def get_async_task_id(async_task) -> int:
    task = asyncio.create_task(async_task())
    task_id = id(task)
    return task_id


async def get_async_task_result(task_id: int) -> Any:
    tasks = asyncio.all_tasks()
    for task in tasks:
        if id(task) == task_id:
            if task.done():
                return task.result()
            else:
                await task
                return task.result()


async def get_async_tasks():
    tasks_list = []
    tasks = asyncio.all_tasks()
    current_task = asyncio.current_task()
    tasks.remove(current_task)
    completed, pending = await asyncio.wait(tasks, timeout=10)
    # completed, pending = await asyncio.wait(tasks, timeout=10, return_when=FIRST_COMPLETED)
    for task in completed:
        tasks_list.append({id(task): 'выполнена'})
    for task in pending:
        tasks_list.append({id(task): 'ожидает выполнения'})
    return tasks_list
