from pydantic import BaseModel
from sqlalchemy import Column , Integer , String
from database import Base

class UserTable(Base):
    __tablename__ ="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
class user_response(BaseModel):
    id:int
    name:str
    email:str
class User(BaseModel):
    name:str
    email:str
    password:str