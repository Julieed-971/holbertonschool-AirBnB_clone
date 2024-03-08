#!/usr/bin/python3
"""Unit tests for the review class"""

import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """Test the review instantiation"""
    def test__init__(self):
        my_review = Review()
        self.assertIsInstance(my_review.place_id, str)
        self.assertIsInstance(my_review.user_id, str)
        self.assertIsInstance(my_review.text, str)
