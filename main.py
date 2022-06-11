from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

@app.get("/user/{user_id}", response_model=User)
def main(user_id: int):
    user = {
        "id": 2,
        "username": "Mike",
        "email": "dfasf@mail.com"
    }
    return user