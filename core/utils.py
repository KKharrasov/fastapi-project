from starlette.requests import Request
from .db import SessionLocal


# def get_db(request: Request):
#     return request.state.db

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
