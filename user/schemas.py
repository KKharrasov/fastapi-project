from pydantic import BaseModel, constr
from typing import Union



BaseModel.Config.orm_mode = True


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=200)
    email: constr(min_length=3, max_length=200)
    id: int
    sup: bool


class UserCreate(BaseModel):
    email: constr(min_length=3, max_length=200)
    username: constr(min_length=3, max_length=200)
    password: constr(min_length=3, max_length=200)


class UserDB(UserCreate):
    pass


class UserList(UserCreate):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
