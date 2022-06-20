from starlette.requests import Request
from .db import SessionLocal


def get_db(request: Request):
    return request.state.db

# Dependency

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
