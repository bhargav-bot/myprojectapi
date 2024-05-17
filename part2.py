from fastapi import FastAPI
from fastapi.params import Body
from fastapi.params import Body, Depends, Header, Path, Query
from pydantic import   BaseModel, Field , EmailStr
from pydantic.types import Json             
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

App=FastAPI()


@App.get("/posts")
def root():
    return {"message": "Hello World"}

@App.post("/posts")
def create_post(post:Post):
    print(post.dict())
    return {"message": "post created"}
