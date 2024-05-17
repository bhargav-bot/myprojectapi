               
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.sqltypes import Boolean
from database import Base
from sqlalchemy import DateTime, Integer, String




class Bhargav(Base):
    __tablename__ = 'bhargav'
    name =Column(String,nullable=False)
    price=Column(Integer,nullable=False)
    id=Column(Integer,primary_key=True,nullable=False)
    onsale=Column(Boolean,server_default='True',nullable=False)
    inventory=Column(Integer,nullable=False) 
    time_stamp=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

class Audi(Base):
    __tablename__='jogi'
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    job=Column(String,nullable=False)
    id=Column(Integer,nullable=False,primary_key=True)


class mercedes(Base):
    __tablename__='whatever'
    name=Column(String,nullable=False)
    id=Column(Integer,nullable=False,primary_key=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
