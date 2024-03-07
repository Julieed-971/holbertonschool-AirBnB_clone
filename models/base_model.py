#!/usr/bin/python3
"""Base class for all the other classes to inherit from"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Method to instantiate an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Return the class description"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update attribute updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = self.__class__.__name__
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        return dict_cpy
