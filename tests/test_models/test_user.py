#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User instantiation"""
    def test__init__(self):
        my_user = User()
        self.assertIsInstance(my_user.email, str)
        self.assertIsInstance(my_user.password, str)
        self.assertIsInstance(my_user.first_name, str)
        self.assertIsInstance(my_user.last_name, str)
