from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db
from app.schemas.crosswalk import CrosswalkSchema, CrosswalkCreate


router = APIRouter()


@router.get("/")
def read_crosswalks(db: Session = Depends(get_db)) -> Any:
    crosswalks = crud.get_crosswalks(db)
    return crosswalks


@router.get("/{id}", response_model=CrosswalkSchema)
def read_crosswalk(id: int, db: Session = Depends(get_db)) -> Any:
    return crud.get_crosswalk(db, id)  # returns null if not found !TODO maybe raise exception


@router.post("/", response_model=CrosswalkSchema)
def create_crosswalk(
    crosswalk: CrosswalkCreate,
    db: Session = Depends(get_db)
) -> Any:
    crosswalk_name = crosswalk.name
    if crud.get_crosswalk_by_name(db, crosswalk_name):
        raise HTTPException(
            status_code=400,
            detail=f"Crosswalk with name ({crosswalk_name}) "
            "is already registered")
    return crud.create_crosswalk(db=db, crosswalk=crosswalk)
