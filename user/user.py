from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt
from core.utils import get_db
from user import service
from core import security
from datetime import timedelta
from user.schemas import UserList, UserCreate, UserUserovich, Token



router = APIRouter()


@router.post("/users/", response_model=UserCreate)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/users/", response_model=List[UserUserovich])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_users(db, skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=UserUserovich)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{username}", response_model=UserUserovich)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = service.get_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(form_data.username, form_data.password, db=Session)
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


@router.get("/users/me/", response_model=UserUserovich)
async def read_users_me(current_user: UserUserovich = Depends(security.get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: UserUserovich = Depends(security.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]
