from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from core.db import SessionLocal
from routes import routes
import uvicorn

from fastapi import Request, Response

from user import models
from core.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)



def run_app():
    app = FastAPI()
    app.include_router(routes)

    return app


if __name__ == '__main__':
    uvicorn.run('main:app',
                host='127.0.0.1',
                port=8000,
                )
else:
    app = run_app()


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


