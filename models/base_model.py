from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """Base class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Method to instantiate an instance of BaseModel"""
        if kwargs:
            self.id = kwargs.get('id', str(uuid4()))
            self.created_at = datetime.strptime(kwargs.get('created_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Return string representation of the instance"""
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
