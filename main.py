from fastapi import FastAPI
from typing import Any, List, Dict
from schemas import GetIDSchema
from service import get_async_task_id, get_async_task_result, get_async_tasks
from task_example import my_async_task

app = FastAPI()


@app.post("/get_id")
async def get_id(request: GetIDSchema) -> int:
    return await get_async_task_id(my_async_task)


@app.get("/get_result/{task_id}")
async def get_result(task_id: int) -> Any:
    return await get_async_task_result(task_id)


@app.get("/get_tasks")
async def get_tasks() -> List[Dict[str, str]]:
    return await get_async_tasks()


@app.get("/")
async def root():
    return {"message": "Hello World"}
