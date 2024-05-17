from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name:str
    age:int
    gender:str=Field(default="male")
    user_id:int=Field(default=0)
class bhargav(BaseModel):
    name:str
    price:int
    id:int
    onsale:bool=False
    inventory:int=0
class test(BaseModel):
    name:str
    price:int
    id:int
    onsale:bool=False
    inventory:int=0
    
    
class post_response(BaseModel):
    name:str
    price:int
    id:int

class get_response(post_response):
    onsale:bool=False
    inventory:int=0
    class config:
        orm_mode =True



class usercreate(BaseModel):
    name:str
    email:str
    password:str
    id:int
class userresponse(usercreate):
    created_at:datetime=datetime.now()

class userlogin(BaseModel):
    email:str
    password:str
    
    class config:
        orm_mode=True

class Token12(BaseModel):
    access_token:str
    token_type:str
    class config:
        orm_mode=True


class tokendata12(BaseModel):
    id:Optional[str]=None
    class config:
        orm_mode=True


  
    
    
    
    
    


