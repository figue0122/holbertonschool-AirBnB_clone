#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting BaseModel"""
    state_id = ""
    name = ""

    def __str__(self):
        """Returns a string representation of the Amenity instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
