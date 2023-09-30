from typing import Annotated

from fastapi import Path, Depends, HTTPException
from . import service
from . import models
from ..dependencies import DBSession


def get_user(db: DBSession, user_id: int = Path(alias="userId")) -> models.User:
    user = service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


User = Annotated[models.User, Depends(get_user)]

