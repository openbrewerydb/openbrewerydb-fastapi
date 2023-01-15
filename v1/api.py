"""
Root API route and other API route imports
"""

from fastapi import APIRouter
from v1.routes import breweries

api_v1_router = APIRouter()

api_v1_router.include_router(breweries.router, prefix="/breweries", tags=["breweries"])


@api_v1_router.get("/")
async def api_v1_root():
    return {"version": 1}
