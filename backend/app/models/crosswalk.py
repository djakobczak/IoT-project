from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class CrosswalkModel(Base):
    __tablename__ = "crosswalks"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)

    statistics = relationship("StatisticsModel", back_populates="crosswalk")
