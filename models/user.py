#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """Return string representation of User"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    