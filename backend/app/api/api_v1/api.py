from fastapi import APIRouter

from app.api.api_v1.endpoints import crosswalks
from app.api.api_v1.endpoints import statistics


api_router = APIRouter()
api_router.include_router(crosswalks.router, prefix="/crosswalks", tags=["crosswalks"])
api_router.include_router(statistics.router, prefix="/statistics", tags=["statistics"])
