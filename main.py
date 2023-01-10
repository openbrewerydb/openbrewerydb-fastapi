"""
FastAPI main application
"""
import os
import time
from pathlib import Path
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from core.config import settings
from v1.api import api_v1_router

BASE_PATH = Path(__file__).resolve().parent
os.environ["TZ"] = settings.TIMEZONE

time.tzset()

def get_application() -> FastAPI:
    """
    Defines the FastAPI Object as an application
    """
    application = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        debug=settings.DEBUG,
        redoc_url=None,
        openapi_url="/v1/openapi.json",
    )

    root_router = APIRouter()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @root_router.get("/", status_code=200)
    async def root(request: Request) -> RedirectResponse:
        """
        Root GET
        """
        return RedirectResponse("https://www.openbrewerydb.org/")

    @root_router.get("/healthcheck", status_code=200)
    async def healthcheck():
        """
        Ping style health check
        """
        return {"status": "ok"}

    application.include_router(api_v1_router, prefix=settings.API_V1_STR)
    application.include_router(root_router)

    return application

app = get_application()
