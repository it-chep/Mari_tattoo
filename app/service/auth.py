import string

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from starlette import status

from app.logger import Logger
from app.repository.cache.cache_work import RedisRepository
from app.repository.sessions.sessions import SessionRepository
from app.repository.users.users import UsersRepository
from app.utils.hash import Hasher
import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
characters = string.ascii_letters + string.digits + string.punctuation
cache = RedisRepository()


async def get_current_user_from_token(user_repo=Depends(UsersRepository), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials, you unauthorized",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(payload)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await user_repo.get_user_by_email(email)

    if user is None:
        raise credentials_exception
    return user


class AuthService:
    def __init__(self, user=Depends(UsersRepository), session=Depends(SessionRepository)):
        self.user = user
        # self.session = session

    async def authenticate_user(self, email: str, password: str):
        user = await self.user.get_user_by_email(email)

        if user is None:
            return
        if not Hasher.verify_password(password, user.hashed_password):
            return

        # random_string = ''.join(random.choice(characters) for _ in range(30))
        # self.session.create_session(session_id=random_string, user=user)
        # Это для админки

        return user


class AdminAuth:

    def __init__(
         self,
         users_repository=Depends(UsersRepository),
         admin_repository=Depends(SessionRepository)
    ):

        self.logger = Logger('admin_service')
        self.users_repository = users_repository
        self.cache = cache
        self.admin_repository = admin_repository

    async def auth_user(self, session_id):
        user = await self.cache.get_value(key=f'{session_id}')
        if user is None:
            user = await self.admin_repository.get_user_from_session_id(session_id)

            if user is None:
                return 403, {"message": "You have not admin cookie"}

            await self.cache.set_value(key=f'{session_id}', value=user, timeout=1209600)

        return 200, {'user': f"{user}"}
