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
    """FileStorage class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}
    CLASS_DICT = {"BaseModel": BaseModel,
                  "User": User,
                  "City": City,
                  "Place": Place,
                  "Review": Review,
                  "State": State,
                  "Amenity": Amenity}

    def all(self):
        """Returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            dict_obj = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
            json.dump(dict_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                cls_name = value["__class__"]
                cls = FileStorage.CLASS_DICT.get(cls_name)
                if cls:
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
