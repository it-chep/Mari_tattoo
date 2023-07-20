from fastapi import APIRouter, Depends

# from app.dependencies import get_tattoo_service
from app.service.tattoo import TattooService

tattoo_router = APIRouter(prefix="/tattoo", tags=["tattoo"])
# service = TattooService()


# @tattoo_router.get("/")
# async def main_tattoo_page():
#     result = service.main_tattoo_page()
#     return result
#
#
# @tattoo_router.get("/calculator")
# async def get_calculate_tattoo():
#     result = service.get_calculate_tattoo()
#     return result
#
#
# @tattoo_router.post("/calculator")
# async def post_calculate_tattoo():
#     result = service.post_calculate_tattoo()
#     return result


@tattoo_router.get("/works")
async def get_tattoo_works(service: TattooService = Depends(TattooService)):
    # print('router')
    result = service.get_all_jobs()
    return result


# @tattoo_router.get("/sketches")
# async def get_tattoo_sketches():
#     result = service.get_tattoo_sketches()
#     return result
#
#
# @tattoo_router.get("/sketches/random")
# async def get_random_sketch():
#     result = service.get_random_sketch()
#     return result
