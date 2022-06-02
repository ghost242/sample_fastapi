from sqlalchemy.orm import Session

from src.models import InsertDevModel
from src.models.schemas import DevModel


def get_dev_model(db: Session, key: str):
    return db.query(DevModel).filter(DevModel.key == key).one()

def create_dev_model(db: Session, model: InsertDevModel):
    record = DevModel(key=model.key, value=model.value)

    res = db.add(record)

    if res:
        return record
    else:
        return None
