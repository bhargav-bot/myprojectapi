from jose import JWTError, jwt
from datetime import datetime,timedelta
import schemes1,schemes2
from schemes1 import *
from schemes2 import *
from schemes1 import tokendata12,Token12
from fastapi import Depends,status,HTTPException
from fastapi.security import oauth2,OAuth2PasswordBearer,OAuth2PasswordRequestForm
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(dat:dict):
    to_encode=dat.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt =jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,cred_exception):
    print("token is {},cred is {}".format(token,cred_exception))
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    print('payload is {}'.format(payload))
    id:str=payload.get('user_id')
    print('id is {}'.format(id))
    
    if id is None:
        raise cred_exception
    else:
        token_data=tokendata12(id=id)
        return token_data

def current_user(token:str=Depends(oauth2_scheme)):
    credential_exception=HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='could not validate the credentials',headers={'WWW-Authenticate':'Bearer'})
    return verify_token(token,credential_exception)
