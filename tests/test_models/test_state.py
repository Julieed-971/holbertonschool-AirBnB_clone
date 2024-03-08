#!/usr/bin/python3
"""Unit tests for the State class"""

import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """Test the State instantiation"""
    def test__init__(self):
        my_state = State()
        self.assertIsInstance(my_state.name, str)
