from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from random import randint
from pydantic.types import conint

class createuser(BaseModel):
    name:str
    type:str
    age:int
    id:int
    class config:
        orm_mode='True'
class returnuser(BaseModel):
    name:str
    type:str
    class config:
        orm_mode='True'


class pokemonlogin(BaseModel):
    name:str
    id:int
    class config:
        orm_mode='True'

class tokendata12(BaseModel):
    id:Optional[str]=None
    class config:
        orm_mode=True

class usercreate(BaseModel):
    id:int
    password:str

class userreturn(usercreate):
    
    class config:
        orm_mode=True
        

class postscreate(BaseModel):
    name:str
    id:int
    
    class config:
        orm_mode=True

class postsreturn(postscreate):
    
    user_id:int
    

class poo(postsreturn):
    Post:postsreturn
    vote:int 
    class config:
        orm_mode=True
class poo2(BaseModel):
    name:str
    id:int
    user_id:int
    owner:postsreturn
    vote:int
    
class vote(BaseModel):
    post_id:int
    dir:int
class SlaveBase(BaseModel):
    id: int
    name: str
    user_id: int
 

class SlaveWithVotes(SlaveBase):
    vote_count: int





