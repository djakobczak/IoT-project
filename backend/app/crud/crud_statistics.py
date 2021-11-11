from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import or_

from app.models.statistics import StatisticsModel
from app.schemas.statistics import StatiscsSchema


def get_statistics(db: Session):
    return db.query(StatisticsModel).all()


def get_crosswalk_statistics(db: Session, crosswalk_id_or_name: str):
    return db.query(StatisticsModel).filter(or_(
        StatisticsModel.crosswalk_name == crosswalk_id_or_name,
        StatisticsModel.crosswalk_id == crosswalk_id_or_name,)).all()


def create_statistics(db: Session, stat: StatiscsSchema):
    db_stat = StatisticsModel(
        crosswalk_name=stat.crosswalk_name,
        timestamp=stat.timestamp,
        pedestrians=stat.pedestrians)
    db.add(db_stat)
    db.commit()
    db.refresh(db_stat)
    return db_stat
