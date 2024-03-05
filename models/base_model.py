#!/usr/bin/python3
"""Base class for all the other classes to inherit from"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """Base class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Method to instantiate an instance of BaseModel"""
        if kwargs is not None:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return the class description"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """Update attribute updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        self.__dict__["__class__"] = 'BaseModel'
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
