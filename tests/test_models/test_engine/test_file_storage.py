#!/usr/bin/python3
"""Unittest for file storage
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import json

class FileStorageTest(unittest.TestCase):
    """unittest for file storage"""

    def all_method_test(self):
        """test all method"""
        storage = FileStorage()
        obj = storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIsNotNone(obj)
        self.assertIs(obj, storage._FileStorage__objects)

    def attr_test(self):
        """test of attrs"""

        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def new_method_test(self):
        """test new method """

        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 54791156
        user.name = "mohamed"
        storage.new(user)
        val = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[val])

    def save_test(self):
        """test save method"""

        fun = self._model.to_dict()
        val = fun['__class__'] + "." + fun['id']
        storage = FileStorage()
        storage.save()
        with open("file.json", 'r') as f:
            data = json.load(f)
        new = data[val]
        for key in new:
            self.assertEqual(fun[key], new[key])

    
    def tests(self):
        """test cases"""

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                self.assertIsInstance(all_objs, dict)
                self.assertIsInstance(obj, BaseModel)
                val = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
                self.assertEqual(str(obj), val)
                self.assertEqual(f"{obj_id}",
                                 f"{obj.__class__.__name__}.{obj.id}")
        except FileNotFoundError:
            self.assertIsInstance(all_objs, dict)
            self.assertEqual(all_objs, {})

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
