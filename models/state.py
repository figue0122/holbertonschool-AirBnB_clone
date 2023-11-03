#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""

    def __str__(self):
        """String representation of the State instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    