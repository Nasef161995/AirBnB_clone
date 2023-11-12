#!/usr/bin/python3
"""Unittest for BaseModel([..])
"""
import unittest
from models.base_model import BaseModel
import uuid


class BaseModelTests(unittest.TestCase):
    """Test BaseModel class"""

    my_model = BaseModel()

    def test_init(self):
        """Test the init of the BaseModel class"""

        data = {"name": "John", "age": 30}
        model = BaseModel(**data)
        self.assertEqual(model.name, "John")
        self.assertEqual(model.age, 30)

    def setUp(self):
        """....."""

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

    def test_id(self):
        """Test if the id attribute of the BaseModel class is a valid UUID"""

        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertEqual(str(uuid.UUID(model.id)), model.id)
        self.assertIsInstance(model.id, str)
        self.assertNotEqual(model.id, '')
        self.assertEqual(str(uuid.UUID(model.id)), model.id)
