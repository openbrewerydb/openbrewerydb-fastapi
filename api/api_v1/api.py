"""
Import all routers together
"""
from fastapi import APIRouter
from api.api_v1.routes import healthcheck

api_router = APIRouter()


api_router.include_router(
    healthcheck.router, prefix="/healthcheck", tags=["healthcheck"]
)
