from fastapi import FastAPI,HTTPException
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
from model import Audi
import model
from schemes2 import abcde
from schemes2 import User,post
from typing import List

import model


from database import engine,get_db
Vum=FastAPI()

model.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn=psycopg2.connect(host='localhost',database ='bhargav',user='postgres',password='Bhargav@1908',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("connection is successful")
        break
    except Exception as error:
        print('connection is failed')
        print(error)
        time.sleep(1)
        print('retrying')
        continue

test=[{'name':'xyz','age':20,'job':'developer','id':1},{'name':'abc','age':25,'id':2,
'job':'manager'}]



def findindex(id):
    for  i,j in enumerate(test):
        if j['id']==id:
            return i
    return None



\


@Vum.get('/final/{id}',response_model=abcde)
def getfirst(id:int,db:Session=Depends(get_db)):
    #print(db.query(model.Audi).filter(model.Audi.id==id))
    #print(db.query(model.Audi).filter(model.Audi.id==id).count())
    qur=db.query(model.Audi).filter(model.Audi.id==id).first()
    if qur is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        return qur
    
@Vum.get('/final/',response_model=List[post])
def getfunc(db:Session=Depends(get_db)):
   
    user=db.query(model.Audi).all()
    
    return user
@Vum.post('/final/')
def postfunc(user:User,db:Session=Depends(get_db),status_code=status.HTTP_201_CREATED):
    db.add(**user.dict())
    db.commit()
    #db.refresh(user )
   # new_user=model.Audi(name=user.name,age=user.age,job=user.job,id=user.id)
   # db.add(new_user)
    #db.commit()
    #db.refresh(new_user)
    return {'text':user.dict()}
@Vum.delete('/final/{user_id}')
def delfunc(user_id:int,db:Session=Depends(get_db),status_code=status.HTTP_204_NO_CONTENT):
    c=db.query(model.Audi).filter(model.Audi.id==user_id).delete()
    #print(db.query(model.Audi).filter(model.Audi.id==user_id).delete())
    #print(type(db.query(model.Audi).filter(model.Audi.id==user_id)))
    if c==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        print('total number of lines deleted:{}'.format(c))
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail='user deleted')
@Vum.put('/final/{user_id}')
def upfunc(user_id:int,user:User,db:Session=Depends(get_db)):
    num=db.query(model.Audi).filter(model.Audi.id==user_id).update(user.dict())
    if num==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        db.commit()
    
    return user.dict()
    
@Vum.get('/io/')
def user_get():
    cursor.execute("""select * from jogi""")
    test=cursor.fetchall()
    return {'test':test}
@Vum.post('/io/')
def user_post(user:User,status_code =status.HTTP_201_CREATED):
    cursor.execute("""INSERT INTO jogi (name, age, job, id) VALUES ( %s,%s,%s,%s) returning *""",(user.name,user.age,user.job,user.id))
    conn.commit()
    test=cursor.fetchone()
    raise HTTPException(status_code=201,detail={'test':test})
@Vum.delete('/io/{user_id}')
def user_delete(user_id:int):
    d=cursor.execute("""Delete from jogi where id ={}""".format(user_id))
    print("value of d is :{}".format(d))
    conn.commit()
    if d==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
@Vum.put('/io/{user_id}')
def update_user(user_id: int,user:User):
    cursor.execute("""update jogi set name=%s,age=%s,job=%s,id=%s where id=%s returning *""",(user.name,user.age,user.job,user.id,str(user_id)))
    updated_user=cursor.fetchone()
    conn.commit()
    print(updated_user)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not found')
    else:
        return {'data':updated_user}
@Vum.get('/info')
def info(): 
    return {'test':test}

@Vum.post('/info',status_code=status.HTTP_201_CREATED)
def insert(user:User):
    test.append(user.dict())
    return {'test':user}

@Vum.delete('/info/{id}')
def delete_test(id:int,status_code=status.HTTP_204_NO_CONTENT):
    c=findindex(id)
    if c is not None:

        test.pop(c)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=404,detail='user not found')
    

@Vum.put('/info/{id}')
def user_test(id:int,user:User):
    c=findindex(id)
    if c is None:
        raise HTTPException(status_code=404,detail="user not found")
    else:
        test[c]=user.dict()
        return {'text': user.dict()}
    
class Ket(BaseModel):
    name:str
    age:int
    job:str
    id:int=0


@Vum.post('/whatever/',status_code=status.HTTP_201_CREATED,response_model=abcde)
def whatever(var:Ket,db:Session=Depends(get_db)):
    db.add(model.Audi(**var.dict()))
    db.commit()
    db.refresh(var)
    return var



