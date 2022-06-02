import logging

from fastapi import FastAPI, Depends

from src.client.crud import create_dev_model, get_dev_model
from src.models import GetDevModel, InsertDevModel
from src.models.database import engine, SessionInst
from src.models.schemas import Base

service_app = FastAPI()

def session_generator():
    sess = SessionInst()

    try:
        yield sess

    finally:
        sess.close()

@service_app.get("/")
async def index():
    return {"message": "Hello world!!"}

@service_app.post("/insert", response_model=InsertDevModel)
async def insert(model: InsertDevModel, sess: SessionInst = Depends(session_generator)):
    res = create_dev_model(sess, model)

    return res

@service_app.get('/{key}', response_model=GetDevModel)
async def find(key: str, sess: SessionInst = Depends(session_generator)):
    res_model = get_dev_model(sess, key)

    return res_model


def service_initializer():
    logging.debug(f"engine: {engine}, SessionInst: {SessionInst}")

    Base.metadata.create_all(bind=engine)
