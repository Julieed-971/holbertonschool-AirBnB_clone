#!/usr/bin/python3
"""Unittests for -Airbnb clone - the console- project"""

import unittest
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the Base class"""
    def test_save(self):
        """Test if updated_at is updated with save()"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

if __name__ == "__main__":
    unittest.main()