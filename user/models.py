from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core.db import Base
from typing import Union



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    full_name: Union[str, None] = None
