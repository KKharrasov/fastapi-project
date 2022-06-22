from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate
from core.security import get_password_hash, ADMIN_LOGIN, ADMIN_PASSWORD



def create_user(db: Session, user: UserCreate):
    user = User(**user.dict())
    if user.username == ADMIN_LOGIN and user.password == ADMIN_PASSWORD:
        user.sup = True
    user.password = get_password_hash(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def is_admin(user: User = Depends(get_user)):
    if not user.sup:
        raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Access denied',
    )
    return user