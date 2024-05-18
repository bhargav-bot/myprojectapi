from pydantic_settings import BaseSettings

class settings(BaseSettings):
    database_hostname:str
    database_password:str
    database_port:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int=30
    class Config:
        env_file = ".env"




setting=settings()

