from typing import Annotated

from fastapi import Depends

from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DBSession = Annotated[SessionLocal, Depends(get_db)]
