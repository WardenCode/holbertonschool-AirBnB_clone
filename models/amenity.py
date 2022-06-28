#!/usr/bin/python3
"""
Class Amenity for AirBnB clone
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel
    """
    name: str = ""
