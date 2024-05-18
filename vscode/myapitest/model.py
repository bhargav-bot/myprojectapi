from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import Boolean
from vscode.myapitest.database import Base
from sqlalchemy import DateTime, Integer, String


class poke(Base):
    __tablename__='pokemon'
    name:str=Column(String,nullable=False,unique=true)
    type:str=Column(String,nullable=False,unique=False)
    age:int=Column(Integer,nullable=False)
    id:int=Column(Integer,primary_key=True)




class Slave(Base):
    __tablename__='posts'
    name:str=Column(String)
    id:int=Column(Integer,primary_key=True)
    user_id:int=Column(Integer,ForeignKey("user.id",ondelete='CASCADE',onupdate='CASCADE'))
    owner=relationship('Master')
class Master(Base):
    __tablename__='user'
    id:int=Column(Integer,primary_key=True)
    password:str=Column(String)

class vote(Base):
    __tablename__="votes"
    post_id:int = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    user_id:int=Column(Integer, ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    

    
    