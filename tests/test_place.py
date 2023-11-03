#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        """ Setup values for testing """
        self.place1 = Place()
        self.place2 = Place()
        self.place2.city_id = "123456"
        self.place2.user_id = "7890"
        self.place2.name = "Beautiful Beach House"
        self.place2.description = "A lovely place by the beach"
        self.place2.number_rooms = 3
        self.place2.number_bathrooms = 2
        self.place2.max_guest = 6
        self.place2.price_by_night = 150
        self.place2.latitude = 37.7749
        self.place2.longitude = -122.4194
        self.place2.amenity_ids = ["wifi", "pool"]

    def test_id(self):
        """ Test id """
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_attributes(self):
        """ Test attributes for Place"""
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertTrue(hasattr(self.place1, "amenity_ids"))

    def test_attributes_default(self):
        """ Test attributes default for Place """
        self.assertEqual(self.place1.city_id, "")
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])  # Change to an empty list

    def test_inheritance(self):
        """ Test inheritance from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_to_dict(self):
        """ Test to_dict for Place """
        expected = {
            "id": self.place2.id,
            "__class__": type(self.place2).__name__,
            "city_id": "123456",
            "user_id": "7890",
            "name": "Beautiful Beach House",
            "description": "A lovely place by the beach",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 6,
            "price_by_night": 150,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenity_ids": ["wifi", "pool"],
            "created_at": self.place2.created_at.isoformat(),
            "updated_at": self.place2.updated_at.isoformat()
        }
        self.assertDictEqual(self.place2.to_dict(), expected)

    def test_str(self):
        """ Test str for the Place """
        expected = "[Place] ({}) {}".format(self.place2.id, self.place2.__dict__)
        self.assertEqual(str(self.place2), expected)

    def test_save(self):
        """ Test save for the Place """
        created_at = self.place1.created_at
        updated_at = self.place1.updated_at
        self.place1.save()
        self.assertEqual(created_at, self.place1.created_at)
        self.assertNotEqual(updated_at, self.place1.updated_at)

if __name__ == '__main__':
    unittest.main()
