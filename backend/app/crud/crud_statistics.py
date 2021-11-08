from sqlalchemy.orm import Session

from app.models.statistics import StatisticsModel
from app.schemas.statistics import StatiscsSchema


def get_statistics(db: Session):
    return db.query(StatisticsModel).all()


def get_crosswalk_statistics(db: Session, crosswalk_id: int):
    return db.query(StatisticsModel).filter(StatisticsModel.crosswalk_id == crosswalk_id).all()


def create_statistics(db: Session, stat: StatiscsSchema):
    db_stat = StatisticsModel(
        crosswalk_id=stat.crosswalk_id,
        timestamp=stat.timestamp,
        pedestrians=stat.pedestrians)
    db.add(db_stat)
    db.commit()
    db.refresh(db_stat)
    return db_stat
