#!/usr/bin/python3
"""Base class for all the other classes to inherit from"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """Base class for all other classes to inherit from"""

    def __init__(self):
        """Method to instantiate an instance of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the class description"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """Update attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        self.__dict__['__class__'] = 'BaseModel'
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
