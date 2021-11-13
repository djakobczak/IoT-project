from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        username=user.username,
        disabled=user.disabled,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(UserModel).all()


def get_user(db: Session, username: str):
    return db.query(UserModel).filter(
        UserModel.username == username).first()
