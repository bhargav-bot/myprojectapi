from pydantic_settings import BaseSettings


class settings(BaseSettings):
    database_hostname:str='c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
    database_password:str='pfc2fb6bc2755d68700ca31d31c66e5f966621007d1bf721338a4544d868755f6'
    database_port:str='5432'
    database_name:str='d7tfu32ti1me77'
    database_username:str='uegsmsrkgaomm8'
    secret_key:str='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'   
    algorithm:str='HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int=60
    #MY_DATABASE_URL:str='postgresql://u32hacvapjkcg0:p214666510362171577c54a7484498cd7f073b5191dcdd181ca8f0de5dc33197e@c97r84s7psuajm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4iao105dgf212'
    class Config:
        env_file = ".env"

    


setting=settings()

