#!/usr/bin/python3
""" Module for Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """Class of review"""
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """String representation of the Review instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
