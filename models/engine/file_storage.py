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
