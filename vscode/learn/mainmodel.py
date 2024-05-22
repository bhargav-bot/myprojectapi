from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt 
from datetime import datetime,timedelta

from datetime import UTC
expiretime=60
algorithm='HS256'
secret_key='patel'
time=datetime.utcnow()+timedelta(expiretime)
myapp=FastAPI()


@myapp.get('/')
def func():
    return "ddddd"


@myapp.get('/login/')
def generate_token():
    token=jwt.encode(expiretime,secret_key,algorithm=algorithm)
    return token

