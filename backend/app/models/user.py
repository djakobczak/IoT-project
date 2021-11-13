from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import Boolean, String

from app.db.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
