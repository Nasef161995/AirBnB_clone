#!/usr/bin/python3
"""Unittest for file storage
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


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

    storage = FileStorage()

    def tests(self):
        """test cases"""

        i = len(self.fs.all())
        _dict = self.storage.all().copy()
        new_model = BaseModel()
        self.storage.new(new_model)

        self.storage.save()

        self.storage.reload()

        count = len(self.storage.all())
        self.assertEqual(count, i + 1)

        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, self.storage.all())

        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.updated_at, new_model.updated_at)
