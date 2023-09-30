from pydantic import BaseModel


class BaseUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str


class UserCreate(BaseUser):
    username: str


class UserUpdate(BaseUser):
    pass
