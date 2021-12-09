from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_active_user, get_db, reusable_oauth2
from app.schemas.crosswalk import CrosswalkSchema, CrosswalkCreate
from app.schemas.user import UserSchema


router = APIRouter()


@router.get("/")
def read_crosswalks(
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_active_user)
)-> Any:
    crosswalks = crud.get_crosswalks(db)
    return crosswalks


@router.get("/{id}", response_model=CrosswalkSchema)
def read_crosswalk(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_active_user)
) -> Any:
    return crud.get_crosswalk(db, id)


@router.post("/", response_model=CrosswalkSchema)
def create_crosswalk(
    crosswalk: CrosswalkCreate,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_active_user)
) -> Any:
    crosswalk_name = crosswalk.name
    if crud.get_crosswalk_by_name(db, crosswalk_name):
        raise HTTPException(
            status_code=400,
            detail=f"Crosswalk with name ({crosswalk_name}) "
            "is already registered")
    return crud.create_crosswalk(db=db, crosswalk=crosswalk)


@router.delete("/{name}", response_model=CrosswalkSchema)
def delete_crosswalk(
    name: str,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_active_user)
) -> Any:
    if not crud.get_crosswalk_by_name(db, name):
        raise HTTPException(status_code=404, detail="Crosswalk not found")
    return crud.delete_crosswalk(db, name)
