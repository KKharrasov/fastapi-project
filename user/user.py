from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.utils import get_db
from user import errors, service
from user.responses import ResultResponse, with_errors
from user.models import User
from user.schemas import *
from .service import get_password_hash, ADMIN_LOGIN, ADMIN_PASSWORD



router = APIRouter()


@router.post('/register', response_model=UserCreate,
            responses=with_errors(errors.bad_token, errors.access_denied, errors.user_already_exists),
            )
def register(
        params: UserCreate,
        db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == params.username).first()
    if user is not None:
        raise errors.user_already_exists()
    user = User(**params.dict())
    if user.username == ADMIN_LOGIN and user.password == ADMIN_PASSWORD:
        user.sup = True
    user.password = get_password_hash(user.password)
    db.add(user)
    db.flush()
    return user


@router.get('/all_users',
            response_model=List[UserBase],
            responses=with_errors(errors.bad_token, errors.access_denied),
            )
def get_all_users(
        db: Session = Depends(get_db),
        admin: User = Depends(service.is_admin)
):
    return db.query(User).all()


@router.post("/token", response_model=AuthToken)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = service.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return service.generate_token(user)


@router.get("/users/me", response_model=UserBase,
            responses=with_errors(errors.bad_token, errors.user_not_found),
            )
async def read_users_me(current_user: UserBase = Depends(service.get_current_user)):
    return current_user


@router.post('/login',
            response_model=AuthToken,
            responses=with_errors(errors.bad_token, errors.login_error),
            )
def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    user_id = service.authenticate_user(username, password, db)
    return service.generate_token(user_id)


@router.post('/refresh',
            response_model=AuthToken,
            responses=with_errors(errors.bad_token),
            )
def refresh_token(
    user: User = Depends(service.verify_refresh_token),
    db: Session = Depends(get_db)
):
    return service.generate_token(user.id)


@router.get('/',
            response_model=ResultResponse,
            responses=with_errors(errors.bad_token, errors.user_not_found),
            )
def is_auth(user: User = Depends(service.get_current_user)):
    return ResultResponse()
