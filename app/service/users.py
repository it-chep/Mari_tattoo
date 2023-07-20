from fastapi import Depends

from app.logger import Logger
from app.repository.cache.cache_work import RedisRepository
from app.repository.users.schemas import ShowUser
from app.repository.users.users import UsersRepository
from app.utils.hash import Hasher


class UsersService:

    def __init__(self):
        pass
