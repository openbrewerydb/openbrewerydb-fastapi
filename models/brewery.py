"""
Brewery SQL model
"""
from sqlalchemy import Integer, String, Column, Float

from app.db.base_class import Base


class Brewery(Base):
    """
    Basic class for a Brewery SQL model object
    """
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brewery_type = Column(String)
    street = Column(String)
    address_2 = Column(String)
    address_3 = Column(String)
    city = Column(String)
    state = Column(String)
    county_province = Column(String)
    postal_code = Column(String)
    website_url = Column(String)
    phone = Column(String)
    country = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
