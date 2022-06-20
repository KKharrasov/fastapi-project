from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.utils import get_db
from user import service
from user.schemas import UserList, UserCreate, User
router = APIRouter()


@router.get("/users/", response_model=List[UserList], response_model_exclude_unset=True)
def user_list(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.post("/users/", response_model=UserCreate)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)



@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_users(db, skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


