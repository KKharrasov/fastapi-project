from pydantic import BaseModel, constr
from enum import Enum

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


class TokenPurpose(str, Enum):
    access = 'access'
    refresh = 'refresh'


class AuthToken(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class AuthTokenPayload(BaseModel):
    user_id: int
    purpose: TokenPurpose


class RefreshTokenParams(BaseModel):
    refresh_token: str
