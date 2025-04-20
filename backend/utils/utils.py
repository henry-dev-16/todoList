from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pass(password:str):
    return pwd_context.hash(password)

def verify_password(non_hashed_pass, hashed_pass):
    return pwd_context.verify(non_hashed_pass, hashed_pass)
