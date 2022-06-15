from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from user import service
from user.schemas import UserCreate, UserList
router = APIRouter()


@router.get("/users/", response_model=List[UserList])
def user_list(db: Session = Depends(get_db)):
    return service.get_user_list(db)


@router.post("/users/")
def user_list(item: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, item)
