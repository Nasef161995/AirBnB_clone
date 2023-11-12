#!/usr/bin/python3
"""Unittest for Amenity([..])
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Unittest for Amenity"""

    def setUp(self):
        """ Unittest for Amenity"""

        self.amenity = Amenity()

    def test_amenity_name(self):
        """ Unittest for Amenity"""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
