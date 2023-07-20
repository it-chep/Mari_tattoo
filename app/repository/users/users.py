from fastapi import Depends

from app.repository.work_session import get_db
from typing import Union, List
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import *
from .models import User


class UsersRepository:
    """Data Access Layer for operating user info"""

    def __init__(self, db=Depends(get_db)):
        self.db = db

    async def get_all_users(self) -> List[ShowUser]:
        users = self.db.query(User).all()
        return [ShowUser.from_orm(user) for user in users]

    async def create_new_user(self, name: str, surname: str, email: str, hashed_password: str):

        new_user = User(
            name=name,
            surname=surname,
            email=email,
            hashed_password=hashed_password,
            roles=[]
        )

        self.db.add(new_user)
        self.db.commit()
        return new_user.user_id

    async def delete_user(self, user_id: UUID):

        query = (
            update(User)
            .where(and_(User.user_id == user_id, User.is_active == True))
            .values(is_active=False)
            .returning(User.user_id)
        )

        res = await self.db.execute(query)
        deleted_user_id_row = res.fetchone()
        if deleted_user_id_row is not None:
            return deleted_user_id_row[0]

    async def get_user_by_id(self, user_id: UUID):

        user = self.db.query(User).filter(User.user_id == user_id).first()

        if user is None:
            return None

        return ShowUser.from_orm(user)

    async def get_user_by_email(self, email: str):

        user = self.db.query(User).filter(User.email == email).first()

        if user is None:
            return None

        # return ShowUser.from_orm(user)
        return user

    async def update_user(self, user_id: UUID, **kwargs):

        query = (
            update(User)
            .where(and_(User.user_id == user_id, User.is_active == True))
            .values(kwargs)
            .returning(User.user_id)
        )

        res = await self.db.execute(query)
        update_user_id_row = res.fetchone()
        if update_user_id_row is not None:
            return update_user_id_row[0]
