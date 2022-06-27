#!/usr/bin/python3
"""

"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
        Class BaseModel to State, City, etc
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of Base Model
        """
        if not(kwargs):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
        else:
            #Consider user crafted JSONs
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["update_at"] = datetime.fromisoformat(kwargs["update_at"])
            self.__dict__.update(**kwargs)


    def __str__(self):
        """
        Unofficial representation of Base Model
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Save the new changes with the actual time
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Representation in a dictionary of the instance
        """
        model = self.__dict__

        model["__class__"] = self.__class__.__name__
        model["created_at"] = model["created_at"].isoformat()
        model["update_at"] = model["update_at"].isoformat()

        return (model)
