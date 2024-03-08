#!/usr/bin/python3
"""Class to create a city"""

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Class to create a city"""

    state_id = BaseModel.id
    name = ""
