from fastapi import APIRouter
from fastapi.responses import JSONResponse

from . import schemas
from . import service
from .dependencies import User
from ..dependencies import DBSession


router = APIRouter()


@router.get('/users/{userId}')
def get_user(user: User):
    return user


@router.delete('/users/{userId}')
def delete_user(db: DBSession,  user: User):
    service.delete_user(db, user)
    return JSONResponse(content={'success': True})


@router.put('/users/{userId}')
def update_user(db: DBSession,  user: User, user_data: schemas.UserUpdate):
    service.update_user(db, user, user_data)
    return JSONResponse(content={'success': True})


@router.post('/users')
def create_user(db: DBSession,  user_data: schemas.UserCreate):
    return service.create_user(db, user_data)

