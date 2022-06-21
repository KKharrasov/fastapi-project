from pydantic import BaseModel, constr
from typing import Union



BaseModel.Config.orm_mode = True


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: constr(min_length=3, max_length=20)
    id: int
    su: bool


class UserCreate(BaseModel):
    email: constr(min_length=3, max_length=20)
    username: constr(min_length=3, max_length=20)
    password: constr(min_length=3, max_length=20)


class UserDB(UserCreate):
    pass


class UserList(UserCreate):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
