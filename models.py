from pydantic import BaseModel
from sqlalchemy import Column , Integer , String
from database import Base

class UserTable(Base):
    __tablename__ ="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    password=Column(String)
class user_response(BaseModel):
    id:int
    name:str
    age:int
class User(BaseModel):
    name:str
    age:int
    password:str