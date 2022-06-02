import logging

from sqlalchemy.orm import as_declarative, declarative_base
from sqlalchemy import Column, Integer, Text

from src.models.database import engine


Base = declarative_base()
# @as_declarative(bind=engine)
# class Base():
#     __tablename__ = ""
#
#     def __init_subclass__(cls, **kwargs):
#         def sep_words(text):
#             start_idx = 0
#             end_idx = 1
#
#             while len(text) > end_idx:
#                 if text[end_idx].isupper():
#                     yield text[start_idx:end_idx]
#                     start_idx = end_idx
#                     end_idx = start_idx + 1
#                 else:
#                     end_idx += 1
#             else:
#                 yield text[start_idx:end_idx]
#
#         cls.__tableanme__ = "TB_" + '_'.join((w.upper() for w in sep_words(cls.__name__)))
#         logging.debug(cls.__tableanme__)

class DevModel(Base):
    __tablename__ = "tb_dev_model"
    __table_args__ = { "schema": "dev_db" }

    idx = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(Text)
    value = Column(Text)
