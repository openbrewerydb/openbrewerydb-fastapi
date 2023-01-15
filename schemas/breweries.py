"""
FastAPI Pydantic schemas for a brewery
"""

from pydantic import BaseModel
from typing import Optional
import datetime


class BreweryBase(BaseModel):
    """
    Brewery base schema via Pydantic
    """

    id: str
    name: str
    brewery_type: str
    street: str
    address_2: Optional[str]
    address_3: Optional[str]
    city: Optional[str]
    state: Optional[str]
    county_province: Optional[str]
    postal_code: str
    website_url: Optional[str]
    phone: Optional[str]
    country: str
    longtitude: Optional[int]
    latitude: Optional[int]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
