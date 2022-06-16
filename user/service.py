from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate
from core.security import get_password_hash

def get_user_list(db: Session):
    return db.query(User).all()

def create_user(db: Session, item: UserCreate):
    user = User(**item.dict())
    user.password = get_password_hash(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user