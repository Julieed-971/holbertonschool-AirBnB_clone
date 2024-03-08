#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import unittest
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_file_path_attribute(self):
        """Test the __file_path attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_attribute(self):
        """Test the __objects attribute"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_method(self):
        """Test the all() method"""
        self.assertEqual(dict, type(storage.all()))

    def test_new_method(self):
        """Test the new() method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn("BaseModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())

    def test_save_method(self):
        """Test the save() method"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        """Test the reload() method"""
        initial_data = {"key": "value"}
        with open(FileStorage._FileStorage__file_path, "w") as f:
            json.dump(initial_data, f)
            storage.reload()
            self.assertEqual(storage.all(), initial_data)


if __name__ == "__main__":
    unittest.main()
