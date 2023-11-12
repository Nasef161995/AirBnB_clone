#!/usr/bin/python3
"""Review module test
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review module test"""

    def test_attributes(self):
        """test cases"""

        model = Review()

        self.assertEqual(model.place_id, '')
        self.assertEqual(model.user_id, '')
        self.assertEqual(model.text, '')
