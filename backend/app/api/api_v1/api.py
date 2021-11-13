from fastapi import APIRouter

from app.api.api_v1.endpoints import crosswalks
from app.api.api_v1.endpoints import statistics
from app.api.api_v1.endpoints import login
from app.api.api_v1.endpoints import users


api_router = APIRouter()
api_router.include_router(crosswalks.router, prefix="/crosswalks", tags=["crosswalks"])
api_router.include_router(statistics.router, prefix="/statistics", tags=["statistics"])
api_router.include_router(login.router, prefix="/login", tags=["security"])
api_router.include_router(users.router, prefix="/users", tags=["security"])
