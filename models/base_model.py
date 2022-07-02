#!/usr/bin/python3
"""
Class BaseModel for AirBnB clone, this class will be used by any other class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Class BaseModel to State, City, etc
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of Base Model
        """
        if not (kwargs):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            # Consider user crafted JSONs
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
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
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Representation in a dictionary of the instance
        """
        model = dict(self.__dict__)

        model["__class__"] = self.__class__.__name__
        model["created_at"] = model["created_at"].isoformat()
        model["updated_at"] = model["updated_at"].isoformat()
        return (model)
