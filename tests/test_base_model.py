#!/usr/bin/python3
"""Unittest Base Model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test the initialization of the BaseModel class."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        my_model = BaseModel(**kwargs)
        for key, value in kwargs.items():
            if key != "__class__":
                self.assertEqual(str(getattr(my_model, key)), value)

    def test_str(self):
        """Test the string representation of BaseModel."""
        my_model = BaseModel()
        expected = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(expected, str(my_model))

    def test_save(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
