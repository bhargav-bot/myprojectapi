from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from jose import JWTError, jwt
import vscode.myapitest.config as config
from config import setting
SQLALCHEMY_DATABASE_URL=f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:5432/{setting.database_name}'



engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()