from fastapi.testclient import TestClient

from src import service_app

client = TestClient(service_app)

def test_app_index():
    response = client.get("/")

    assert response.json() == {"message": "Hello world!!"}
