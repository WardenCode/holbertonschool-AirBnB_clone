#!/usr/bin/python3
"""
Manage the File Storage for the class Base Model
"""
import json
from os.path import exists
import models


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
        Adds a new instance in the obj __objects (to convert into JSON)
        Args:
            - obj: Instance of Base Model
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects.update({f"{obj_name}.{obj.id}": obj})

    def save(self):
        """Writes the obj FileStorage.__objects into a JSON file"""
        save_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as file:
            file.write(json.dumps(save_dict, indent=4, sort_keys=True))

    def reload(self):
        """Loads the data of a JSON file into the program"""
        path = FileStorage.__file_path
        if (exists(path)):
            with open(path, 'r', encoding="utf-8") as file:
                text = file.read()
                if (len(text)):
                    objects = json.loads(text)
                    items = objects.items()
                    classes = models.classes
                    load = {k: classes[v['__class__']](**v) for k, v in items}
                    FileStorage.__objects.update(**load)
