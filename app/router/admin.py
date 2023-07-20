from uuid import UUID

from fastapi import APIRouter, Depends, Request

from app.admin_service.admin_users import AdminUsers

admin_router = APIRouter(prefix='/admin', tags=['admin'])


@admin_router.get('/')
async def admin_main_page(service=Depends(AdminUsers), ):
    return


@admin_router.get('/users')
async def get_all_users(request: Request, service=Depends(AdminUsers), ):

    return {'cookie': request.cookies}


@admin_router.get('/users/{userID}')
async def get_user_by_id(request: Request, userID: UUID, service=Depends(AdminUsers), ):

    return userID


@admin_router.post('/users/{userID}')
async def create_user(request: Request, userID: UUID, service=Depends(AdminUsers), ):
    return


@admin_router.put('/users/{userID}')
async def admin_main_page(request: Request, service=Depends(AdminUsers), ):
    return


@admin_router.delete('/users/{userID}')
async def admin_main_page(request: Request, service=Depends(AdminUsers), ):
    return
