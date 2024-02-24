#!/usr/bin/python3
"""This is a state Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    This is the class for amenity
    """
    __tablename__ = 'amenities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
