#!/usr/bin/python3
"""Unit tests for the city class"""

import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """Test the city instantiation"""
    def test__init__(self):
        my_city = City()
        self.assertIsInstance(my_city.state_id, str)
        self.assertIsInstance(my_city.name, str)
