#!/usr/bin/python3
"""Unit tests for the place class"""

import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """Test the place instantiation"""
    def test__init__(self):
        my_place = Place()
        self.assertIsInstance(my_place.city_id, str)
        self.assertIsInstance(my_place.user_id, str)
        self.assertIsInstance(my_place.name, str)
        self.assertIsInstance(my_place.description, str)
        self.assertIsInstance(my_place.number_rooms, int)
        self.assertIsInstance(my_place.number_bathrooms, int)
        self.assertIsInstance(my_place.max_guest, int)
        self.assertIsInstance(my_place.price_by_night, int)
        self.assertIsInstance(my_place.latitude, float)
        self.assertIsInstance(my_place.longitude, float)
        self.assertIsInstance(my_place.amenity_ids, list)
        
