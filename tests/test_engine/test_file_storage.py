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
        i = len(self.storage.all())
        old_dict = self.storage.all().copy()
        model = BaseModel()
        self.storage.new(model)

        self.storage.save()

        self.storage.reload()

        count = len(self.storage.all())
        self.assertEqual(count, i + 1)

        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

        obj = self.storage.all()[key]
        self.assertEqual(obj.updated_at, model.updated_at)
