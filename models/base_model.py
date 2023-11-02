#!/sur/bin/python3
""" Base_models Module"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = "BaseModel"
        obj_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict
