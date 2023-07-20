from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.repository.users.schemas import UserCreate, UpdateUserRequest, UpdatedUserResponse
from app.service.auth import AuthService
from app.service.users import UsersService
from app.logger import Logger


users_router = APIRouter(prefix='/users', tags=['users'])
users_logger = Logger('users_logger')


@users_router.get('/get_all_users')
async def get_all_users(service=Depends(UsersService), ):
    users = await service.get_all_users()
    return users


@users_router.get('/get_user_by_id')
async def get_user_by_id(user_id: UUID, service=Depends(UsersService), ):
    user = await service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"User with id {user_id} not found."
        )
    return user


@users_router.get('/get_user_by_email')
async def get_user_by_email(email, service=Depends(UsersService), ):
    user = await service.get_user_by_email(email)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"User with id {email} not found."
        )
    return user


@users_router.post('/create_new_user')
async def create_new_user(body: UserCreate, service=Depends(UsersService), ):
    result = await service.create_new_user(
        name=body.name,
        surname=body.surname,
        email=body.email,
        password=body.password,
    )

    return result


@users_router.patch('/update_user')
async def update_user(user_id: UUID, body: UpdateUserRequest, service=Depends(UsersService),
                      current_user=Depends(AuthService), ) -> UpdatedUserResponse:
    pass
