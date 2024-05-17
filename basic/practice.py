from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from typing import List
from typing import Dict
from typing import Any
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel,Field,EmailStr
from pydantic.types import Json




app = FastAPI()
@app.get("/")
def get_user():
    return {
        "name": "John",
        "age": 30,
        "gender": "male"
    }

class User(BaseModel):
    name: str
    age: int 
    gender: str

@app.post("/")
def create_user(user: User):
    print(user.name)
    print(user.age)
    print(user.gender)
    return "hey"
