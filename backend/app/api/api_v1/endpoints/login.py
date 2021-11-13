from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.core.security import verify_password
from app.schemas.token import Token


router = APIRouter()


@router.post("/access-token")
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
