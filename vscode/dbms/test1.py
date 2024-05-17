import psycopg2
from fastapi import FastAPI,Response,status,HTTPException,APIRouter,Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from model import *
from schemes1 import *
from database import *
from schemes2 import *
import oauth2c
from oauth2c import *

from fastapi import APIRouter
from sqlalchemy.orm import Session
from model import  *
from database import get_db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import Boolean
from database import Base
from sqlalchemy import DateTime, Integer, String
import model
import oauth2c
from oauth2c import *

router = APIRouter(
    prefix='/google.com',tags=['google.com']
)
@router.get('/',response_model=list[get_response]) 
def get_test(db:Session=Depends(get_db),):
    get_detail =db.query(model.Bhargav).all() 
    return get_detail
@router.get('/{id}/',response_model=get_response)
def get_res(id:int,db:Session=Depends(get_db)):
    qu=db.query(model.Bhargav).filter(model.Bhargav.id==id).first()
    if qu is not None:

        return qu
    else:
        raise HTTPException(status_code=404,detail='user does not exist')


@router.post('/test/',status_code=status.HTTP_201_CREATED,response_model=post_response)
def post_test(vr:test,db:Session=Depends(get_db)):

    new_post =model.Bhargav(name=vr.name,price=vr.price,id=vr.id,onsale=vr.onsale,inventory=vr.inventory)
    db.add(new_post)
    db.commit()
    
    db.refresh(new_post)
  
    return new_post
@router.delete('/test/{id}')
def delete_test(id:int,db:Session=Depends(get_db)):
    c=db.query(model.Bhargav).filter(model.Bhargav.id==id).delete()
    print(c)
    db.commit()
    if c == 0:
        raise HTTPException(status_code=404,detail="user not found")
    else:
        raise HTTPException(status_code=204)
@router.put('/test/{id}')
def put_test(id:int,user:test,db:Session=Depends(get_db)):
    c=db.query(model.Bhargav).filter(model.Bhargav.id==id).update(user.dict())
    print(c)
    if c ==0:
        raise HTTPException(status_code=404,detail="user not found")
    else:
        db.commit()
        return {"data":user }



