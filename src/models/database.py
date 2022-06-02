import logging
import os
import dotenv

from sqlalchemy.pool import QueuePool
from sqlalchemy.engine import create_engine, URL, Engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

engine: Engine = create_engine(
    URL(
        drivername="postgresql+pg8000",
        username=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        database=os.getenv("PG_DATABASE"),
        query="",
    ),
    pool_size=10,
    pool_recycle=3600,
    pool_timeout=60,
    poolclass=QueuePool,
)

SessionInst: sessionmaker = sessionmaker(bind=engine)

with engine.connect() as conn:
    if not conn.dialect.has_schema(conn, "dev_db"):
        conn.execute(CreateSchema("dev_db"))

logging.debug(f"engine: {engine}, SessionInst: {SessionInst}")
