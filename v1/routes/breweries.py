"""
All breweries endpoints
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def endpoint():
    """
    Ping style health check
    """
    return {"endpoint": "breweries"}
