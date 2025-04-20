from fastapi import APIRouter, status, Depends
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from schemas.users import User, CreateUser
from config.db import get_db
from utils.utils import hash_pass
from utils.auth import get_current_user
from models.users import UserTable

user = APIRouter(tags=["user"])

@user.post('/user', status_code=status.HTTP_201_CREATED,response_model=User)
def create_users(user:CreateUser, db: Session = Depends(get_db)):
    hashed_pass = hash_pass(user.password)
    new_user = user.model_dump()
    new_user.update({"created_at":datetime.now(timezone.utc),"password":hashed_pass})
    new_user = UserTable(**new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.get("/users/me", response_model=User)
def read_users_me(user: User = Depends(get_current_user),db: Session = Depends(get_db)):
    """
    Get current user details
    """
    return user