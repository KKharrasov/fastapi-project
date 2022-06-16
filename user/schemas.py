from pydantic import BaseModel
from typing import Union



class UserIn(BaseModel):    # авторизация
    # username: str
    password: str
    email: str
    #full_name: Union[str, None] = None

    class Config:
        orm_mode = True

class UserCreate(BaseModel):    # регистрация
    username: str
    password: str
    email: str
    full_name: Union[str, None] = None

    class Config:
        orm_mode = True


class UserList(UserCreate):
    id: int


# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: Union[str, None] = None

