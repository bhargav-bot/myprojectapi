from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import Depends,status,HTTPException
from fastapi.security import oauth2,OAuth2PasswordBearer,OAuth2PasswordRequestForm
from config import setting,settings,BaseSettings
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.ACCESS_TOKEN_EXPIRE_MINUTES

from pydantic import BaseModel,Field
from typing import Optional

from database import *




def create_token(data:dict):
    my_var=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    my_var.update({'exp':expire})
    token=jwt.encode(my_var,SECRET_KEY,algorithm=ALGORITHM)
    return token
    
def checktoken(token:str=Depends(oauth2_scheme)):
    my_var=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    var=my_var.get('user_id')
    print(var)
    if var is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='could not validate the credentials',headers={'WWW-Authenticate':'Bearer'})
    else:
        return True
def check_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('user_id')
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail="Invalid credentials")
        print("Decoded Token Payload:", payload)  # Log decoded payload for debugging
        print("User ID:", user_id)  # Print user_id value

        return int(user_id)
    except JWTError as e:
        
        user_id = None  # Assign a default value if decoding fails
        print(user_id)
        
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"JWT Error: {str(e)} and user_id not available")





