from pydantic import BaseModel
from datetime import datetime
from typing import Union



class User(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None


class UserCreate():
    password: str


class UserList():
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInDB(User):
    hashed_password: str