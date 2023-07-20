import uuid
from enum import Enum

from sqlalchemy import Column, Boolean, String
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from app.repository.work_session import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    verify_token = Column(String, nullable=True)
