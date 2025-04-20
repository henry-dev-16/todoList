from datetime import timedelta, datetime, timezone

from fastapi import Depends , HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from schemas.users import DataToken, User
from sqlalchemy.orm import Session

from config.db import get_db
from models.users import UserTable




oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = "882d73930425bf05647e456240f07ba81d24ab54c77d67accb7b5c71a3b07fd6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "expire":expire.strftime("%Y-%m-%d %H:%M:%S")
    })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token_access(token:str, credentials_exceptions):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exceptions
        token_data = DataToken(id=id)
    except JWTError as e:
        print(e)
        raise credentials_exceptions
    return token_data


def get_current_user(db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)) -> User:
    credentials_excetion = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not validate credentials", headers={"www-Authenticate":"Bearer"})
    token = verify_token_access(token, credentials_excetion)

    user = db.query(UserTable).filter(UserTable.id == token.id).first()
    return user