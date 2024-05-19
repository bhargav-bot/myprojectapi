from pydantic_settings import BaseSettings

class settings(BaseSettings):
    database_hostname:str='c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
    database_password:str='pe81786f684fb21802ce708580682c5ab971d8f4a0aba762bcff135d08275abf5'
    database_port:str='5432'
    database_name:str='dfbotrhe8efpjq'
    database_username:str='u2dq1tjhc90b09'
    secret_key:str='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    algorithm:str='HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int=60
    class Config:
        env_file = ".env"




setting=settings()

