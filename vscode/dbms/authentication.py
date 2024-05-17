from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from database import get_db
from schemes1 import *
from schemes2 import *
from model import *
import model
from utilities import *
from passlib.context import CryptContext
import oauth2c
from oauth2c import *
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



router=APIRouter(

)
@router.post('/login')
def posta(user:OAuth2PasswordRequestForm=Depends(),db:session=Depends(get_db)):
    '''
    this returns the dictonary containing username:username ,password:password
    so for the user variable in the function we can not use the user.email we need to use user.username
    you can not add it in json file you have to add it in form section of the post request
    '''
    stor=db.query(model.mercedes).filter(model.mercedes.email==user.username).first()
    if stor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='wrong username or password')
    else:
        e=pwd_context.verify(user.password,stor.password)
        if e is False:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='wrong username or password!!! ')
        else:
            access_token=create_access_token({"user_id":user.username})
            return {"access_token":access_token,"token_type":"bearer"}


