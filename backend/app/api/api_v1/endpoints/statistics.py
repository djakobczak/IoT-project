from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db
from app.schemas.statistics import StatiscsCreate


router = APIRouter()


@router.get("/")
def read_statistics(
    crosswalk_id: Optional[int] = None, 
    db: Session = Depends(get_db)
) -> Any:  # !TODO change to id_or_name
    if crosswalk_id:
        stats = crud.get_crosswalk_statistics(db, crosswalk_id)
    else:
        stats = crud.get_statistics(db)
    return stats


@router.post("/")
def create_statistics(stat: StatiscsCreate, db: Session = Depends(get_db)) -> Any:
    corss_id = stat.crosswalk_id
    crosswalks_ids = [cross.id for cross in crud.get_crosswalks(db)]
    if corss_id not in crosswalks_ids:
        raise HTTPException(
            status_code=404,
            detail=f"Crosswalk with id ({corss_id}) is not registered")

    return crud.create_statistics(db=db, stat=stat)
