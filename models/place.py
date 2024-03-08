#!/usr/bin/python3
"""Class to create a place"""

from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """Class to create a place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    lonngitude = 0.0
    amenity_ids = []
