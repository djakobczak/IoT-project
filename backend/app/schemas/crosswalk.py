from typing import List, Optional

from pydantic import BaseModel


# common for read/write
class CrosswalkBase(BaseModel):
    address: str


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
