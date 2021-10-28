from sqlalchemy import Column, Integer, String

from app.db.database import Base


class CrosswalkModel(Base):
    __tablename__ = "crosswalks"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
