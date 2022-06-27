#!/usr/bin/python3
"""

"""
import json
from os.path import exists
#from models.base_model import BaseModel


class FileStorage():
	""""""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		""""""
		return (FileStorage.__objects)

	def new(self, obj):
		""""""
		FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()})

	def save(self):
		""""""
		with open(FileStorage.__file_path, 'w+', encoding='utf-8') as file:
			file.write(json.dumps(FileStorage.__objects))

	def reload(self):
		""""""
		path = FileStorage.__file_path
		if(exists(path)):
			with open(path, 'r', encoding="utf-8") as file:
				objects = json.loads(file.read())
				FileStorage.__objects.update(**objects)
