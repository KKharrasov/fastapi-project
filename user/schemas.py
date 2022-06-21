from pydantic import BaseModel
from typing import Union



class UserBase(BaseModel):
    email: str
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUserovich(UserBase):
    id: int
    disabled: Union[bool, None] = None

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
