#!/usr/bin/python3
"""
Manage the File Storage for the class Base Model
"""
import json
from os.path import exists
# from models.base_model import BaseModel


class FileStorage():
    """
    Class FileStorage for manage the instance created by BaseModel
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all the objects in the JSON file"""
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Adds a new instances in the obj FileStorage.__objects (to convert into JSON)
        Args:
            - obj: Instance of Base Model
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects.update({f"{obj_name}.{obj.id}": obj.to_dict()})

    def save(self):
        """Writes the obj FileStorage.__objects into a JSON file"""
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as file:
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Loads the data of a JSON file into the program"""
        path = FileStorage.__file_path
        if (exists(path)):
            with open(path, 'r', encoding="utf-8") as file:
                text = file.read()
                if (len(text)):
                    objects = json.loads(text)
                    FileStorage.__objects.update(**objects)
