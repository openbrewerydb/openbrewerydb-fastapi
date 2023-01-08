"""
FastAPI Pydantic schemas for a brewery
"""

from pydantic import BaseModel

class BreweryBase(BaseModel):
    """
    Brewery base schema via Pydantic
    """
    name: int
    brewery_type: str
    street: str | None
    address_2: str | None
    address_3: str | None
    city: str | None
    state: str | None
    county_province: str | None
    postal_code: str | None
    website_url: str | None
    phone: str | None
    county: str | None
    longtitude: int | None
    latitude: int | None

# Properties to receive via API on creation
class BreweryCreate(BreweryBase):
    submitter_id: int

# Properties to receive via API on update
class BreweryUpdate(BreweryBase):
    id: int

class BreweryInDBBase(BreweryBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

# Additional properties stored in DB but not returned by API
class BreweryInDB(BreweryInDBBase):
    ...

# Additional properties to return via API
class Brewery(BreweryInDBBase):
    ...

class BrewerySearchResults(BaseModel):
    results: list[Brewery]
