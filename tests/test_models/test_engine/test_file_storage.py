#!/usr/bin/python3
"""Test module for FileStorage"""


import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def test_file_path(self):
        """Test the __file_path attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects(self):
        """Test the __objects attribute"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """Test the all() method"""
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """Test the new() method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn("BaseModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())

    def test_save(self):
        """Test the save() method"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """Test the reload() method"""
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
