from pydantic import BaseModel

class BaseDevModel(BaseModel):
    idx: int

class InsertDevModel(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = True

class GetDevModel(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = False
