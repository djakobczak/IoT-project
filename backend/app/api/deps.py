from datetime import datetime, timedelta
from typing import Generator, Optional

from fastapi import status, HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm.session import Session


from app import crud
from app.core.settings import settings
from app.db.database import SessionLocal
from app.schemas.user import UserInDB, UserSchema
from app.schemas.token import TokenPayload


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

SECRET_KEY = "6916cf97-1fab-4483-a94b-e82130b19283"  # !TODO fix
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


fake_users_db = {
    "johndoe": {
        "username": "john",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "hashed_password": "fakehashedsecret2",
        "disabled": False,
    },
}


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(username=payload.get("sub"))
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_user(db, token_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
