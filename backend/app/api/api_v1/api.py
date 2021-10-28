from fastapi import APIRouter

from app.api.api_v1.endpoints import crosswalks


api_router = APIRouter()
api_router.include_router(crosswalks.router, prefix="/crosswalks", tags=["crosswalks"])
