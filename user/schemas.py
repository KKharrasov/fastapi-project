from pydantic import BaseModel
from datetime import datetime



class UserBase(BaseModel):
    date: datetime

class UserCreate(UserBase):
    pass

class UserList(UserBase):
    id: int
