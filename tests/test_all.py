# from fastapi.testclient import TestClient
#
# from main import app
#
# client = TestClient(app)
#
# task_id = []
#
#
# def test_get_id():
#     response = client.post(f"/get_id",
#                            json={
#                                "x": 1,
#                                "y": 2,
#                                "operator": "+"
#                            })
#     task_id.append(response.json())
#     assert response.status_code == 200
#     # пропустил проверку тела ответа, не вижу смысла сюда дублировать функцию для получения id
#
#
# async def test_get_result():
#     response = client.get(f"/get_result/{task_id[0]}")
#     assert response.status_code == 200
#     assert response.json() == 42
#
#
# async def test_get_tasks():
#     response = client.get(f"/get_tasks/")
#     assert response.status_code == 200
#     # и здесь пропускаю проверку

import pytest
from httpx import AsyncClient

from main import app

task_id = []


@pytest.mark.anyio
async def test_get_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/get_id",
                                 json={
                                     "x": 1,
                                     "y": 2,
                                     "operator": "+"
                                 })
    task_id.append(response.json())
    assert response.status_code == 200
        # пропустил проверку тела ответа, не вижу смысла сюда дублировать функцию для получения id


@pytest.mark.anyio
async def test_get_result():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/get_result/{task_id[0]}")
    assert response.status_code == 200
    assert response.json() == 42


@pytest.mark.anyio
async def test_get_tasks():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/get_tasks/")
    assert response.status_code == 200
    # и здесь пропускаю проверку
