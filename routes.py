from fastapi import APIRouter
from user import user


routes = APIRouter()

routes.include_router(user.router)


# routes.include_router(user.router, prefix="/user")

