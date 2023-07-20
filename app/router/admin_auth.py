from fastapi import APIRouter

auth_admin_router = APIRouter(prefix='/auth_admin', tags=['auth_admin'])


@auth_admin_router.get('/login')
async def admin_get_login():
    return


@auth_admin_router.post('/login')
async def admin_post_login():
    return


@auth_admin_router.get('/logout')
async def admin_get_login():
    return


@auth_admin_router.post('/logout')
async def admin_post_login():
    return
