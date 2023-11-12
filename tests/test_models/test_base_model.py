#!/usr/bin/python3
"""Unittest for BaseModel([..])
"""
import unittest
from models.base_model import BaseModel



class BaseModelTests(unittest.TestCase):
    def test_init(self):
        data = {"name": "John", "age": 30}
        model = BaseModel(**data)
        self.assertEqual(model.name, "John")
        self.assertEqual(model.age, 30)
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        self.model.save()
        self.assertTrue(self.model.id is not None)