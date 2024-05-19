from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from jose import JWTError, jwt
import vscode.myapitest.config as config
from vscode.myapitest.config import setting
SQLALCHEMY_DATABASE_URL=f'postgresql://u32hacvapjkcg0:p214666510362171577c54a7484498cd7f073b5191dcdd181ca8f0de5dc33197e@c97r84s7psuajm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4iao105dgf212'



engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()