#!/usr/bin/python3
"""
Class State for AirBnB clone
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State that inherits from BaseModel
    """
    name: str = ""
