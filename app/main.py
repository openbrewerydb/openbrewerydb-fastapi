"""
FastAPI main application
"""
import os
import time
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from app.core.config import settings
from app.api.api_v1.api import api_router

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))
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
    async def root(request: Request) -> dict:
        """
        Root GET
        """
        return TEMPLATES.TemplateResponse("index.html", {"request": request})

    application.include_router(api_router, prefix=settings.API_V1_STR)
    application.include_router(root_router)

    return application


app = get_application()
