from sqlalchemy.orm import Session

from src.models import GetDevModel, InsertDevModel
from src.models.schemas import DevModel


def get_dev_model(db: Session, key: str):
    record = db.query(DevModel).filter(DevModel.key == key).first()

    return GetDevModel(key=record.key, value=record.value)


def create_dev_model(db: Session, model: InsertDevModel):
    record = DevModel(key=model.key, value=model.value)

    try:
        db.add(record)
    except:
        db.rollback()
    else:
        db.commit()

        return record
