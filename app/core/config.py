"""
Environments and configuration file
"""
import logging
import os
import secrets
from enum import Enum
from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class EnvironmentEnum(str, Enum):
    """
    Enumerate the application environments
    """

    PRODUCTION = "production"
    DEVELOPMENT = "development"


class GlobalConfig(BaseSettings):
    """
    Base configuration to be modified by specific environments
    """

    TITLE: str = "Open Brewery DB REST API"
    DESCRIPTION: str = "A REST API for Open Brewery DB"
    JWT_SECRET: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM = "HS256"
    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"
    # DB_USER: str = os.environ["DB_USER"]
    # DB_PWD: str = os.environ["DB_PWD"]
    # DB_HOST: str = os.environ["DB_HOST"]
    # DB_NAME: str = os.environ["DB_NAME"]
    # DATABASE_URL: Optional[
    #     PostgresDsn
    # ] = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:5432/{DB_NAME}"
    # DB_ECHO_LOG: bool = False
    # Api V1 prefix
    API_V1_STR = "/v1"

    # @property
    # def async_database_url(self) -> Optional[str]:
    #     """
    #     Define the database URL as a property of the configuration
    #     """
    #     return (
    #         self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    #         if self.DATABASE_URL
    #         else self.DATABASE_URL
    #     )

    class Config:
        """
        Define configuration as case sensitive
        """

        case_sensitive = True


class DevelopmentConfig(GlobalConfig):
    """
    Development configurations
    """

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.DEVELOPMENT


class ProdConfig(GlobalConfig):
    """
    Production configurations
    """

    DEBUG: bool = False
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.PRODUCTION


class FactoryConfig:
    """
    Class creates a factory for configurations
    """

    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == EnvironmentEnum.DEVELOPMENT.value:
            return DevelopmentConfig()
        return ProdConfig()


@lru_cache()
def get_configuration() -> GlobalConfig:
    """
    Generate a configuration based on environment
    """
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()
