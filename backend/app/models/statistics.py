from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String

from app.db.database import Base


class StatisticsModel(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    crosswalk_id = Column(Integer, ForeignKey("crosswalks.id"))  # !TODO remove or register with crud create
    crosswalk_name = Column(String, ForeignKey("crosswalks.name"))
    pedestrians = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True)

    rel_crosswalk_id = relationship("CrosswalkModel", backref="statistics_cross_id", foreign_keys=[crosswalk_id])
    rel_crosswalk_name = relationship("CrosswalkModel", backref="statistics_cross_name", foreign_keys=[crosswalk_name])
