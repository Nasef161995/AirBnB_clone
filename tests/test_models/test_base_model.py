#!/usr/bin/python3
"""Unittest for BaseModel([..])
"""
import unittest
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """Test BaseModel class"""

    def test_init(self):
        data = {"name": "John", "age": 30}
        model = BaseModel(**data)
        self.assertEqual(model.name, "John")
        self.assertEqual(model.age, 30)
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        """Test the save method of the BaseModel class"""

        self.model.save()
        self.assertTrue(self.model.id is not None)
    
    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""

        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        model = BaseModel()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertIn('BaseModel', model_str)
        self.assertIn('id', model_str)
        self.assertIn('created_at', model_str)
        self.assertIn('updated_at', model_str)    
