from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class StatisticsModel(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    crosswalk_id = Column(Integer, ForeignKey("crosswalks.id"))
    pedestrians = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True)

    crosswalk = relationship("CrosswalkModel", back_populates="statistics")
