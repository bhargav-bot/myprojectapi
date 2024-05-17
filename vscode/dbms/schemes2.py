from pydantic import BaseModel,Field
class User(BaseModel):
    name:str
    age:int
    job:str
    id:int=0

class post(BaseModel):
    name:str
    age:int


class abcde(post):
    id:int
    job:str
 

