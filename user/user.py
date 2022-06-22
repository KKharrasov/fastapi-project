from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from core.utils import get_db
from user import service
from core import security
from datetime import timedelta
from user.schemas import UserCreate, UserBase, Token



router = APIRouter()


@router.post("/users/", response_model=UserCreate)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/users/", response_model=List[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_users(db, skip=skip, limit=limit)


# @router.get("/users/getuserbyid/{user_id}", response_model=UserBase)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = service.get_user(db, id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @router.get("/users/getuserbyusername/{username}", response_model=UserBase)
# def read_user(username: str, db: Session = Depends(get_db)):
#     db_user = service.get_username(db, username=username)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = security.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserBase)
async def read_users_me(current_user: UserBase = Depends(security.get_current_user)):
    return current_user


