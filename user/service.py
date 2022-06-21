from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate
from core.security import get_password_hash



def create_user(db: Session, user: UserCreate):
    user = User(**user.dict())
    user.password = get_password_hash(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
