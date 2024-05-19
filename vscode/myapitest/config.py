from pydantic_settings import BaseSettings

class settings(BaseSettings):
    database_hostname:str='c97r84s7psuajm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
    database_password:str='p214666510362171577c54a7484498cd7f073b5191dcdd181ca8f0de5dc33197e'
    database_port:str='5432'
    database_name:str='d4iao105dgf212'
    database_username:str='u32hacvapjkcg0'
    secret_key:str='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    algorithm:str='HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int=60
    MY_DATABASE_URL:str='postgrdes://u32hacvapjkcg0:p214666510362171577c54a7484498cd7f073b5191dcdd181ca8f0de5dc33197e@c97r84s7psuajm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4iao105dgf212'
    class Config:
        env_file = ".env"




setting=settings()

