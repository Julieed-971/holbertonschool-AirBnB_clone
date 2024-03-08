#!/usr/bin/python3
"""Unit tests for the amenity class"""

import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Test the amenity instantiation"""
    def test__init__(self):
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.name, str)
