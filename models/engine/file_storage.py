#!/usr/bin/python3
"""FileStorage Module"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        self.CLASS_DICT = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "Amenity": Amenity
        }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            dict_obj = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(dict_obj, f)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value["__class__"]
                    cls = self.CLASS_DICT.get(cls_name)
                    if cls:
                        instance = cls(**value)
                        self.__objects[key] = instance
