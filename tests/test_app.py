from fastapi.testclient import TestClient

from app import service_initializer
from src import service_app

client = TestClient(service_app)

def pytest_sessionstart():
    service_initializer()

def test_app_index():
    response = client.get("/")

    assert response.json() == {"message": "Hello world!!"}


def test_insert():
    response_post = client.post("/insert", json={"key": "Hello", "value": "World!"})

    assert response_post.json() == {"key": "Hello", "value": "World!"}

    response_get = client.get("/Hello")

    assert response_get.json() == {"key": "Hello", "value": "World!"}