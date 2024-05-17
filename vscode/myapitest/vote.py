from fastapi import FastAPI,HTTPException,APIRouter,Depends,status,HTTPException
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
from fastapi import FastAPI,HTTPException,APIRouter,Depends
from passlib.context import CryptContext
import schemas,database,model,oauthfile
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from pydantic_settings import BaseSettings
from config import setting,settings,BaseSettings
import schemas
from mainfile import Session
from database import get_db
from oauthfile import check_token

router=APIRouter(prefix='/vote')

@router.post('/',status_code=status.HTTP_201_CREATED)
def votefunc(user:schemas.vote,db:Session=Depends(get_db),d=Depends(check_token)):
    check=db.query(model.vote).filter(model.vote.post_id==user.post_id,model.vote.user_id==d)
    value=check.first()
    if (user.dir==1):
        if value:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='{} has already liked the photo'.format(d))
        
        new =model.vote(post_id=user.post_id,user_id=d)
        db.add(new)
        db.commit()
        return 'successfully liked the picture'
    
    else:
        if not value:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='vote does not exist')
        else:
            check.delete(synchronize_session=False)
            db.commit()
        return 'suceefully unliked the post'
    

    
        

