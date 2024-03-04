#!/usr/bin/python3
"""Unittests for -Airbnb clone - the console- project"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the Base class"""
    bm1 = BaseModel()
    bm2 = BaseModel()

    def test__init__(self):
        """Test BaseModel uuid"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.id, str)

        """Test BaseModel created_at time"""
        self.assertTrue(hasattr(self.bm1, "created_at"))

        """Test BaseModel updated_at time"""
        self.assertTrue(hasattr(self.bm1, "updated_at"))

    def __str__(self):
        """Test if __str__ format is correct"""
        self.assertIsInstance(self.bm1.__str__, "[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def test_save(self):
        """Test if updated_at is updated"""
        self.bm1.save()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_to_dict(self):
        """Test BaseModel to_dict module"""
        self.bm1.to_dict()
        self.assertIsInstance(self.bm1.__dict__, dict)
