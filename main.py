from aioredis import Redis
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.middlewares import authenticate, work_time, admin_authenticate
from app.repository.cache.cache_config import redis_client
from app.router.admin import admin_router
from app.router.admin_auth import auth_admin_router
from app.router.auth import auth_router
from app.router.tattoo import tattoo_router
from fastapi.responses import RedirectResponse
from app.router.users import users_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(auth_admin_router)
app.include_router(tattoo_router)
app.include_router(users_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

app.middleware("http")(admin_authenticate)
app.middleware("http")(authenticate)
app.middleware("http")(work_time)


@app.get('/')
async def main():
    return RedirectResponse('/tattoo')


# Подключаемся к Redis при старте приложения
@app.on_event("startup")
async def startup_event():
    await redis_client.establish_connection()


# Закрываем соединение с Redis при остановке приложения
@app.on_event("shutdown")
async def shutdown_event():
    await redis_client.close_connection()
