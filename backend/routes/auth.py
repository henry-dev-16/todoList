from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from utils.auth import create_access_token
from schemas.users import Token
from models.users import UserTable
from utils.utils import verify_password
from config.db import get_db


auth_routers = APIRouter(tags=["Authentication"])


@auth_routers.post("/login", response_model=Token)
def login(userdetails: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(UserTable).filter((UserTable.email == userdetails.username)
            | (UserTable.username == userdetails.username)
        ).first()
    print("lslsls", user, userdetails.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"The User Does not exist")
    if not verify_password(userdetails.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Password do not match")
    
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type":"bearer"}
