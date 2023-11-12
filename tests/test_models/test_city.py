#!/usr/bin/python3
"""Unittest for city([..])
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Unittest for City"""

    def setUp(self):
        """ Unittest for City"""

        self.city = City()

    def test_city_state_id(self):
        """ Unittest for id"""

        self.assertEqual(self.city.state_id, "")

    def test_city_name(self):
        """ Unittest for name"""

        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
