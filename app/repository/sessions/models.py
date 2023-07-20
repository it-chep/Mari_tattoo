import uuid
from datetime import timedelta, datetime
from enum import Enum

from sqlalchemy import Column, Boolean, String, ForeignKey, Integer, TIMESTAMP, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship

from app.repository.work_session import Base


class Session(Base):
    __tablename__ = 'Сессии пользователей'

    id = Column(Integer, primary_key=True)
    session_id = Column(String, unique=True)
    user_id = Column(UUID, ForeignKey('users.user_id'))
    status = Column(Boolean(create_constraint=True), default=True)
    user = relationship('User')
    expire_date = Column(DateTime, default=datetime.now() + timedelta(days=40)) # пока не добавил в миграции


