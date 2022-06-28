#!/usr/bin/python3
"""
Class Review for AirBnB clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
