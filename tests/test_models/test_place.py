#!/usr/bin/python3
"""place module test
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """place module test"""

    def test_attributes(self):
        """test cases"""

        my_model = Place()
        self.assertEqual(my_model.name, '')
        self.assertEqual(my_model.city_id, '')
        self.assertEqual(my_model.user_id, '')
        self.assertEqual(my_model.max_guest, 0)
        self.assertEqual(my_model.description, '')
        self.assertEqual(my_model.number_rooms, 0)
        self.assertEqual(my_model.number_bathrooms, 0)
        self.assertEqual(my_model.longitude, 0.0)
        self.assertEqual(my_model.price_by_night, 0)
        self.assertEqual(my_model.latitude, 0.0)
        self.assertEqual(my_model.amenity_ids, [])
