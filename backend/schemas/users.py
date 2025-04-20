from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
import datetime

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    created_at: Optional[datetime.datetime]= None
    updated_at: Optional[datetime.datetime]=None

    class Config:
        from_attributes = True

class CreateUser(BaseModel):
    email:str
    username:str
    password:str

class UserLogin(BaseModel):
    email:str
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class DataToken(BaseModel):
    id:Optional[int] = None
