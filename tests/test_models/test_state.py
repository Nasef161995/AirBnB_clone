#!/usr/bin/python3
""" State module test
"""

import unittest
from models.state import State


class StateTest(unittest.TestCase):
    """State module test"""

    def testcase(self):
        """........"""

        model = State()

        self.assertEqual(model.name, '')
