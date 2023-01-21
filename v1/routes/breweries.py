"""
All breweries endpoints
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=200)
async def get_all_breweries():
    return {"endpoint": "get_all_breweries"}


@router.post("/", status_code=201)
async def post_breweries():
    return {"endpoint": "post_breweries"}


@router.get("/random/", status_code=200)
async def get_random_brewery():
    return {"endpoint": "get_random_brewery"}


@router.get("/meta/", status_code=200)
async def meta():
    return {"endpoint": "metadata"}


@router.delete("/{id}/", status_code=501)
async def delete_brewery_by_id():
    return {"endpoint": "delete_brewery_by_id"}


@router.get("/{id}/", status_code=200)
async def get_brewery_by_id():
    return {"endpoint": "get_brewery_by_id"}


@router.post("/{id}/", status_code=201)
async def update_brewery_by_id():
    return {"endpoint": "update_brewery_by_id"}
