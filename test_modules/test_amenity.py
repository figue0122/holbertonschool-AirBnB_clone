#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """ Setup values for testing """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.amenity2.name = "HWIFI"
        self.amenity2.save()

    def test_id(self):
        """ Test id """
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_attributes(self):
        """ Test attributes for Amenity """
        self.assertTrue(hasattr(self.amenity1, "name"))

    def test_attributes_default(self):
        """ Test attributes default for Amenity """
        self.assertEqual(self.amenity1.name, "")

    def test_inheritance(self):
        """ Test inheritance from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_to_dict(self):
        """ Test dict for Amenity """
        expected = {
            "id": self.amenity2.id,
            "__class__": type(self.amenity2).__name__,
            "name": "HWIFI",
            "created_at": self.amenity2.created_at.isoformat(),
            "updated_at": self.amenity2.updated_at.isoformat()
        }
        self.assertDictEqual(self.amenity2.to_dict(), expected)

    def test_str(self):
        """ Test str for Amenity """
        expected = f"[{type(self.amenity2).__name__}] ({self.amenity2.id}) {self.amenity2.__dict__}"
        self.assertEqual(str(self.amenity2), expected)

    def test_save(self):
        """ Test save for Amenity """
        created_at = self.amenity1.created_at
        updated_at = self.amenity1.updated_at
        self.amenity1.save()
        self.assertEqual(created_at, self.amenity1.created_at)
        self.assertNotEqual(updated_at, self.amenity1.updated_at)

if __name__ == '__main__':
    unittest.main()