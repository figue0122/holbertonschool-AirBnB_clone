#!/usr/bin/python3
"""Unittest for FileStorage class"""

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
    """This class handles serialization and deserialization of instances."""

    # File path to store serialized data
    __file_path = "file.json"

    # Dictionary to hold objects
    __objects = {}

    # Dictionary mapping class names to classes
    CLASS_DICT = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "Amenity": Amenity
    }

    def all(self):
        """Returns stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """objects to the JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            # Create a dictionary with object IDs as keys and their serialized representations as values
            dict_obj = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(dict_obj, f)

    def reload(self):
        """Data from the JSON file to objects."""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                # Load the objects from the file
                objs = json.load(f)

            # Reconstruct the objects, data and store them in the dictionary
            for key, value in objs.items():
                cls_name = value["__class__"]
                cls = FileStorage.CLASS_DICT.get(cls_name)
                if cls:
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
