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

    def save(self):
        """Update attribute updated_at with the current datetime and save changes"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # Other methods omitted for brevity

if __name__ == "__main__":
    # Add any tests or execution logic here
    pass
