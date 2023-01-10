from fastapi import APIRouter

api_v1_router = APIRouter()

@api_v1_router.get("/")
async def api_v1_root():
    return {"version": 1}