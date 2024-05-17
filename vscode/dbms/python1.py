from fastapi import FastAPI,HTTPException,APIRouter
from pydantic import BaseModel
from typing import Optional
from typing import List
from typing import Dict
from typing import Any
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel,Field,EmailStr
from pydantic.types import Json
from fastapi import Response,status
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
from passlib.context import CryptContext
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utilities import *
from model import *
from database import *
from authentication import*
import test1   
import authentication
import oauth2c
import model
import schemes1
from schemes1 import test,bhargav,User,post_response,get_response,usercreate,userresponse
from database import engine,get_db
from fastapi.security import oauth2,OAuth2PasswordRequestForm,OAuth2AuthorizationCodeBearer
from jose import JWTError,jwt
from datetime import datetime,UTC,timedelta
model.Base.metadata.create_all(bind=engine)




while True:
    try:
        conn=psycopg2.connect(host='localhost',database='bhargav',user='postgres',password='Bhargav@1908',cursor_factory=RealDictCursor)   
        cursor=conn.cursor()
       
        print("database connection successful")
        break
    except Exception as error:
        print("database connection failed")
        print(error)
        time.sleep(2)
        print("retrying")
        continue

my_post= [{"name":"myname", "age":20, "gender":"male","user_id":0},{"name":"yourname", "age":20, "gender":"male", "user_id":1}] #this is to return the value when use get function to the terminal

app = FastAPI(
prefix='/ketan',tags= ['ketan','user1']
)
app.include_router(test1.router)
app.include_router(authentication.router)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
def create_acc(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encoded=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded

def verify_token(token:str,exception_create):
    find_user=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    d=find_user.get('user_id')
    if d is None:
        raise exception_create
    else:
        return True

def create_fuss(token:str=Depends(oauth2_scheme)):
    cred=HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    print(token)
    return verify_token(token,cred)

def find_id(id):#look for the specific user if found then only return that user 
    for i in my_post:
        if i["user_id"]==id:   
            return i
    return None
def find_index(id):#look for the specific user if found then only return that user 
    for i,j in enumerate(cursor):
        if j["id"]==id:   
            return i 
        else:
            return None

@app.post('/login123')
def login33(var:OAuth2PasswordRequestForm=Depends(),db:session=Depends(get_db)):
    e=db.query(model.mercedes).filter(model.mercedes.email==var.username).first()
    print(e)
    if e is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    d=pwd_context.verify(var.password,e.password)
    if d is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        token=create_acc({'user_id':var.username})
        return {'access_token':token,'token_type':'Bearer'}

@app.get('user1/{id}')
def get_user(id:int,db:Session=Depends(get_db)):
    getuser=db.query(model.mercedes).filter(model.mercedes.id==id).first()
    #if getuser is not  None:
    return getuser







@app.post('/adduser1/',status_code=status.HTTP_201_CREATED,response_model=userresponse)
def adduser(vr:usercreate,db:Session=Depends(get_db),val:bool=Depends(create_fuss)):
    vr.password=pwd_context.hash(vr.password)
    new_post =model.mercedes(name=vr.name,id=vr.id ,email=vr.email, password=vr.password)
 
    db.add(new_post)
    db.commit()
    
    db.refresh(new_post)
   
    return new_post
@app.get('/user/{id}',response_model=userresponse)
def gettt(id:int,db:Session=Depends(get_db)):
    get_user123=db.query(model.mercedes).filter(model.mercedes.id==id).first()
    return get_user123



    













@app.get("/ketan/")
def get_user():
    cursor.execute("""SELECT * FROM bhargav""")
    post=cursor.fetchall()
    #print(post)    
    return {"data":post}#it is gonna return array in the json that we define above my_post

@app.get("/ketan/latest")
def get_user2():
    return {"data":my_post[len(my_post)-1]}#prints the last entry in array

@app.get("/ketan/{user_id}")
def get_user(user_id:int,response:Response):#will only accept the int user_id not anything else

    cursor.execute("""select * from bhargav where id={}""".format(user_id))
    user_detail=cursor.fetchone()
    if user_detail is None:
        '''
        response.status_code=404#it returns the status code 404 if the user is not found so atleast the front end can know that.
        return {"data":"user not found"}
        '''
        raise HTTPException(status_code=404,detail="user not found")
    else:
        return {"data":user_detail} 
@app.post("/ketan/",status_code=status.HTTP_201_CREATED)#make sure it returns 201 for the post function instead of 200,status_code is default parameter you need to use that
def post_user(post:bhargav):
    conn.commit()
    cursor.execute("""insert into bhargav (name,price,id,onsale,inventory) values ( %s,%s,%s,%s,%s) returning *""",(post.name,post.price,post.id,post.onsale,post.inventory))
    new_post=cursor.fetchone()
    print("data inserted")
    return {"data":new_post}
def update_value(user_id:int,user:User):
    for i,j in enumerate(my_post):
        if j['user_id']==user_id:
            my_post[i]=user.dict()
            return my_post[i]
        else :
            return None
@app.put("/ketan/{user_id}")
def user_update(user_id:int,user:bhargav):
    cursor.execute("""update bhargav set name={},price={},id={},onsale={},inventory={} where id={} returning *""".format(user.name,user.price,user.id,user.onsale,user.inventory,user_id))
    conn.commit()
    new_user=cursor.fetchone()
    print("number of updated lines {}".format(cursor.rowcount))
    if new_user is None:
        raise HTTPException(status_code=404,detail="user not found")
    return {"data":new_user}
    
@app.delete('/ketan/{user_id}')
def  delete_user(user_id:int):
    
    cursor.execute("""delete from bhargav where id = {} returning *""".format(user_id))
    lines_deleted=cursor.fetchone()
    if lines_deleted is None:
        raise HTTPException(status_code=404,detail="user not found")
    else :
        conn.commit()
        raise HTTPException(status_code=204)

        
    #else:
        
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found!')
    #    return 5
    



 




    







 






  
    

    



    

