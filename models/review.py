#!/usr/bin/python3
"""Class to create a review"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Class to create a city"""

    place_id = ""
    user_id = ""
    text = ""
