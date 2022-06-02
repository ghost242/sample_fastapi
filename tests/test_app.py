from uuid import uuid4

from src.models.database import SessionInst
from src.models.schemas import DevModel
from src import service_app

from fastapi.testclient import TestClient
from pytest import fixture

client = TestClient(service_app)

@fixture()
def model_data():
    return {"key": str(uuid4()), "value": "World!"}

@fixture()
def session():
    return SessionInst()

def test_app_index():
    response = client.get("/")

    assert response.json() == {"message": "Hello world!!"}


def test_insert(session, model_data):
    response_post = client.post("/insert", json=model_data)

    assert response_post.json() == model_data

    records = session.query(DevModel).filter(DevModel.key==model_data['key']).all()

    assert len(records) > 0

def test_get(session, model_data):
    record = DevModel(key=str(uuid4()), value="This is value column.")
    session.add(record)
    session.commit()

    response_get = client.get(f"/{record.key}").json()

    assert response_get["key"] == record.key
    assert response_get["value"] == record.value
