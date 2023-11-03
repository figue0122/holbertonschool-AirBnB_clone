#!/usr/bin/python3
"""Base_Models Module"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModels class"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModels instance"""
        if kwargs:
            # For each key in the dictionary, set the attribute with \
            # the associated value.
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert string datetime to datetime object.
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                # Check if 'id' is not in kwargs, then assign it.
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            # Check if 'created_at' is not in kwargs, then assign it.
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.now()
            # Check if 'updated_at' is not in kwargs, then assign it
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.now()
            if not kwargs:
                models.storage.new(self)
        else:
            """initialize variables"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns class, Id and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Saves current time to updated_at"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Create a dictionary and save current data in it"""
        class_dict = dict(self.__dict__)
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict

