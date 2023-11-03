#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.id = "123"

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""
        self.storage.new(self.obj)
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.new(self.obj)
        self.storage.save()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test reload method"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
