from fastapi import FastAPI,HTTPException,APIRouter,Depends
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from pydantic_settings import BaseSettings
from vscode.myapitest.config import setting,settings,BaseSettings
from sqlalchemy import func


from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional
from typing import List
from typing import Dict
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from typing import Any
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel,Field,EmailStr
from pydantic.types import Json
from fastapi import Response,status
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from jose import JWTError,jwt
from datetime import datetime,UTC,timedelta
import vscode.myapitest.model as model

import vscode.myapitest.database as database
import vscode.myapitest.schemas as schemas
from schemas import createuser,pokemonlogin,returnuser,poo
import vscode.myapitest.oauthfile as oauthfile
from oauthfile import checktoken
from database import engine
model.Base.metadata.create_all(bind=engine)
from oauthfile import *
import vscode.myapitest.schemas as schemas
from schemas import *
from database import *
from sqlalchemy.orm import sessionmaker,Session

from database import get_db
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
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import func as sql_func

from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import Boolean
from database import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import session
from jose import JWTError, jwt  
from fastapi.security import oauth2,OAuth2PasswordBearer,OAuth2PasswordRequestForm
from oauthfile import checktoken,check_token,create_token
from vote import router

from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import Depends,status,HTTPException
from fastapi.security import oauth2,OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
dog=FastAPI()

dog.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    





while True:
    try:
        conn=psycopg2.connect(host='localhost',database='mydatabase',user='postgres',password='Bhargav@1908',cursor_factory=RealDictCursor)   
        cursor=conn.cursor()
       
        print("database connection successful")
        break
    except Exception as error:
        print("database connection failed123erghehgifr")
        print(error)
        time.sleep(2)
        print("retrying")
        continue
dog.post('/ppp/')
def fff():
    return 'ppp'


dog.get('/a')
def fffff():
    return 'pppp'
dog.include_router(router)

@dog.get('/patel/',response_model=list[returnuser])
def fum2(var:createuser,db:Session=Depends(get_db),varvar=Depends(check_token)):
    d=db.query(model.poke).all()
    return d
@dog.put('/update/')
def func(var:createuser,db:Session=Depends(get_db)):
    d=db.query(model.poke).filter(model.poke.id==var.id)
    if d is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='ewgrh')
    else:
        db.query(model.poke).filter(model.poke.id==var.id).update(var.dict())


@dog.post('/po/',status_code=status.HTTP_201_CREATED,response_model=returnuser)
def func(user:createuser,db:Session=Depends(get_db),varvar=Depends(check_token)):
    my_user=model.poke(name=user.name,age=user.age,type=user.type,id=user.id)
    db.add(my_user)
    db.commit()
    db.refresh(my_user)
    return my_user
@dog.post('/login/')
def userlogin(var:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    vari=db.query(model.poke).filter(model.poke.id==var.password)
    if vari is None:
        raise HTTPException(status=404)
    else:
        token=create_token({'user_id':var.password})
    return {'token':token,"token_type":"bearer"}


@dog.get('/getpost',response_model=list[postsreturn])
def ff(db:Session=Depends(get_db),d=Depends(check_token)):
    v=db.query(model.Slave).filter(model.Master.id==int(d)).all()
    return v
@dog.get('/getuser',response_model=list[userreturn])
def f2(db:Session=Depends(get_db),d=Depends(check_token)):
    v=db.query(model.Master).all()
    
    return v

class SlaveOut(BaseModel):
    id: int
    name: str
    user_id: int
    vote: int
    owner: str
    post_count: int

    class Config:
        orm_mode = True
@dog.get('/getpost123', response_model=List[poo])
def f2(db: Session = Depends(get_db)):
    try:
        result = (
            db.query(model.Slave, sql_func.count(model.vote.post_id))
            .outerjoin(model.vote, model.Slave.id == model.vote.post_id)
            .group_by(model.Slave.id)
            
        )

        # Convert tuple to list of poo objects directly
        return [
            poo(
                Post=postsreturn(
                    id=slave.id,
                    name=slave.name,
                    user_id=slave.user_id,
                    owner=slave.owner
                    
                ),
                vote=vote_count
            )
            for slave, vote_count in result
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@dog.get('/getpost12345')
def fff2():
    cursor.execute("""SELECT public.posts.name AS posts_name, public.posts.id AS posts_id, public.posts.user_id AS posts_user_id, count(votes.post_id) AS count_1 
FROM public.posts LEFT OUTER JOIN public.votes ON public.posts.id = public.votes.post_id GROUP BY public.posts.id""")
    d=cursor.fetchall()
    return d
    
@dog.get('/getpost12345')
def f2(db:Session=Depends(get_db)): 
    #v=db.query(model.Slave).all()
    
    #print(dir(sql_func))
    result=db.query(model.Slave,sql_func.count(model.vote.post_id).label('vote')).join(model.vote, model.Slave.id ==model.vote.post_id,isouter=True).group_by(model.Slave.id).all()
 
    return result



@dog.get('/getpost1234')
def f2(db: Session = Depends(get_db)):
    try:
        # Perform the query
        result = (
            db.query(model.Slave, sql_func.count(model.vote.post_id))
            .outerjoin(model.vote, model.Slave.id == model.vote.post_id)
            .group_by(model.Slave.id)
            
        )
        print(type(result))
        # Convert list of tuples to list of dictionaries
        response = [
            {
                "slave": {
                    "id": slave.id,
                    "name": slave.name,
                    "user_id": slave.user_id,
                    "owner":slave.owner
                
                    # Include other necessary fields from Slave model
                },
                "vote_count": vote_count
            }
            for slave, vote_count in result
        ]
        
        # Ensure the response is JSON-serializable
        return jsonable_encoder(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@dog.get('/getuser/query',response_model=list[userreturn])
def f2(db:Session=Depends(get_db),limit:int=10,skip:int=0,search:Optional[str]=" "):
    v=db.query(model.Master).filter(model.Master.password.contains(search)).limit(limit).offset(skip).all()
    
    return v


@dog.post('/user/',status_code=status.HTTP_201_CREATED)
def func(user:usercreate,db:Session=Depends(get_db)):
    my_user=model.Master(password=user.password,id=user.id)
    db.add(my_user)
    db.commit()

@dog.post('/posts/',status_code=status.HTTP_201_CREATED)
def func12(user:postscreate,db:Session=Depends(get_db),d=Depends(check_token)):
    
    my_user=model.Slave(name=user.name,id=user.id,user_id=d)
    db.add(my_user)
    db.commit()
    db.refresh(my_user)
    return my_user


@dog.delete('/deleteuser/{id}')
def ffun(id:int,db:Session=Depends(get_db),d:int=Depends(check_token)):
    e=db.query(model.Master).filter(model.Master.id==d).first()
    if id==d and e is not None:
        #print('type of d {}and type of e.id {}'.format(type(d),type(e.id)))
        e=db.query(model.Master).filter(model.Master.id==d).delete()
        #print(e)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user does not have access")
    return e

    











