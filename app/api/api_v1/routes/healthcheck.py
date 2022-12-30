"""
All components from modules to make REST API routes for healthchecks
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def healthcheck():
    """
    Ping style health check
    """
    return {"status": "ok"}
