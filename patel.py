from fastapi import FastAPI
from fastapi.params import Body
from fastapi.params import Body, Depends, Header, Path, Query
from pydantic import   BaseModel, Field , EmailStr
from pydantic.types import Json             
from typing import Optional

app = FastAPI()
class postf(BaseModel):#this is called pydantic this is used to control what value user must add and what not
    name:str
    surname:str
    published:bool = True
#option value if the value is not given then it is going to be true and if the value is given then it will follow the value
    rating:Optional[int] = None
    #optional field if no value is given then the default value is none and it is not even visible



@app.get("/ketan")
def root():
    return {"message": "welcome to my  api",
            "name": "Bhargav", 
            "age": "22",
            "surname" : "patel"
            }

@app.get("/bhargav/patel/about")
def about():
    return {"message": "about me",
            "name": "Bhargav", 
            "age": "22",
            "surname" : "patel"
            }    
@app.post("/ketan")
def post(new_var:postf):#this is called pydantic this is used to control what value user must add and what not
    print(new_var)
    print(dict(new_var))  #to convert pydantic to dictonary model
    print(new_var.dict()) #to convert pydantic to dictonary model
    print(new_var.name)
    print(new_var)

    print(type(new_var))
    print("published value:"+str(new_var.published))
    print("rating dvalue:"+str(new_var.rating))

    
    return "hi"


    