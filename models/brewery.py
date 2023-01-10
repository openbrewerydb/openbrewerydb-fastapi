"""
Brewery SQL model
"""
from sqlalchemy import Integer, String, Column, Float, DateTime

from app.db.base_class import Base

import datetime


class Brewery(Base):
    """
    Basic class for a Brewery SQL model object
    """

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
    brewery_type = Column(String(128))
    street = Column(String(128), nullable=True)
    address_2 = Column(String(128), nullable=True)
    address_3 = Column(String(128), nullable=True)
    city = Column(String(128))
    state = Column(String(128), nullable=True)
    county_province = Column(String(128), nullable=True)
    postal_code = Column(String(128))
    website_url = Column(String(128), nullable=True)
    phone = Column(String(128), nullable=True)
    country = Column(String(128))
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
