from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    disabled: Optional[bool] = None


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    pass
