from pydantic import BaseModel
from typing import Union



class User(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None

    class Config:
        orm_mode = True

class UserCreate(User):
    password: str


class UserList(User):
    id: int


# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: Union[str, None] = None
#
#
# class UserInDB(User):
#     hashed_password: str