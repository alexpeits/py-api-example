from uuid import uuid4

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, nullable=False, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    addresses = relationship("Address", back_populates="user")
