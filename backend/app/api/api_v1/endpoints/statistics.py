from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db
from app.schemas.statistics import StatiscsCreate


router = APIRouter()


@router.get("/")
def read_statistics(
    crosswalk_id_or_name: Optional[str] = None,
    db: Session = Depends(get_db)
) -> Any:
    if crosswalk_id_or_name:
        stats = crud.get_crosswalk_statistics(db, crosswalk_id_or_name)
    else:
        stats = crud.get_statistics(db)
    return stats


@router.post("/")
def create_statistics(stat: StatiscsCreate, db: Session = Depends(get_db)) -> Any:
    cross_name = stat.crosswalk_name  #!TODO map crosswalk id to name and add it
    crosswalks_names = [cross.name for cross in crud.get_crosswalks(db)]
    if cross_name not in crosswalks_names:
        raise HTTPException(
            status_code=404,
            detail=f"Crosswalk with name ({cross_name}) is not registered")

    return crud.create_statistics(db=db, stat=stat)
