from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(UUID, nullable=False, primary_key=True, default=uuid4)
    address = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="addresses")
