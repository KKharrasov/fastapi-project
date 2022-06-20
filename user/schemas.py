from pydantic import BaseModel
from typing import Union



class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
#    is_active: bool

    class Config:
        orm_mode = True

class UserDB(UserCreate):
    pass


class UserList(UserCreate):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

