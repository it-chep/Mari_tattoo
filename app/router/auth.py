from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

import settings
from app.service.auth import AuthService, oauth2_scheme, get_current_user_from_token
from app.utils.jwt_token import create_access_token

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.get('/login')
async def get_login(user=Depends(get_current_user_from_token), token: str = Depends(oauth2_scheme)):
    # user = await auth_service.get_current_user_from_token(token),
    if user is None:
        user = ''
    return {'Пользователь': f'{user}'}


@auth_router.post('/login')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), auth_service=Depends(AuthService)):
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=90)
    access_token = create_access_token(
        data={"sub": user.email, "other_custom_data": ['mari_tatoo']},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get('/logout')
async def get_logout():
    return


@auth_router.post('/logout')
async def post_logout():
    return
