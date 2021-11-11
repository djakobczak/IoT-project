from typing import Optional

from pydantic import BaseModel


# common for read/write
class CrosswalkBase(BaseModel):
    name: str
    description: Optional[str]


# specific for creating
class CrosswalkCreate(CrosswalkBase):
    pass


# reading from our API
class CrosswalkSchema(CrosswalkBase):
    id: int

    class Config:
        # https://python101.readthedocs.io/pl/latest/bazy/orm/
        # treat db records as objects e.g. cross.id
        orm_mode = True
