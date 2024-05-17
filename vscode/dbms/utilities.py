from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password:str):
    rav= pwd_context.hash(password)
    return rav


def passwordcheck(hashpass,plainpass):
    return pwd_context.verify(hashpass,plainpass)






