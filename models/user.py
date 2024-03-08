#!/usr/bin/python3
"""Class to create a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to create a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
