from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_active_user, get_db
from app.schemas.user import UserCreate, UserSchema


router = APIRouter()


@router.get("/me")
def read_users_me(
    current_user: UserSchema = Depends(get_current_active_user)
):
    return current_user


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
) -> Any:
    username = user.username
    db_usernames = [user.username for user in crud.get_users(db)]
    if username in db_usernames:
        raise HTTPException(
            status_code=400,
            detail=f"User with name ({username}) already exists")
    return crud.create_user(db, user)


@router.get("/")
def get_users(
    db: Session = Depends(get_db),
) -> Any:
    return crud.get_users(db)
