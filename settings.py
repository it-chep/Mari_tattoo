"""File with settings and configs for the project"""
import os
from dotenv import load_dotenv
from envparse import Env

load_dotenv()
env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres",
)

SECRET_KEY = os.getenv('SECRET_KEY')
ADMIN_SECRET_KEY = os.getenv('ADMIN_SECRET_KEY')
ALGORITHM = "HS256"

