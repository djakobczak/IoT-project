from sqlalchemy.orm import Session

from app.models.crosswalk import CrosswalkModel
from app.schemas.crosswalk import CrosswalkSchema


def get_crosswalks(db: Session):
    return db.query(CrosswalkModel).all()


def get_crosswalk(db: Session, crosswalk_id: int):
    return db.query(CrosswalkModel).filter(CrosswalkModel.id == crosswalk_id).first()


def get_crosswalk_by_name(db: Session, crosswalk_name: str):
    return db.query(CrosswalkModel).filter(CrosswalkModel.name == crosswalk_name).first()


def create_crosswalk(db: Session, crosswalk: CrosswalkSchema):
    db_crosswalk = CrosswalkModel(
        name=crosswalk.name,
        description=crosswalk.description)
    db.add(db_crosswalk)
    db.commit()
    db.refresh(db_crosswalk)
    return db_crosswalk
