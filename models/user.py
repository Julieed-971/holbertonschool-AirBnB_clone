#!/usr/bin/python3
"""Class to create a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to create a user"""
    def __init__(self, *args, **kwargs):
        """Instantiate a user instance"""
        super().__init__(*args, **kwargs)
        self.email = str()
        self.password = str()
        self.first_name = str()
        self.last_name = str()
