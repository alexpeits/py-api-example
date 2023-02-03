from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DB_URI

engine = create_engine(DB_URI)


def create_session():
    return Session(engine)
