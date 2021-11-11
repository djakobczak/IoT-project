from datetime import datetime

from pydantic import BaseModel


class StatiscsBase(BaseModel):
    crosswalk_name: str
    timestamp: datetime   # maybe change to start-end, but it requires more from client side
    pedestrians: int


class StatiscsCreate(StatiscsBase):
    pass


class StatiscsSchema(StatiscsBase):
    id: int

    class Config:
        orm_mode = True
