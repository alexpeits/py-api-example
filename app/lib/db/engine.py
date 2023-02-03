from sqlalchemy import create_engine

from app.config import DB_URI

engine = create_engine(DB_URI)
