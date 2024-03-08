#!/usr/bin/python3
"""Class to create a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to create a user"""
    def __init__(self, *args, **kwargs):
        """Instantiate a user instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
