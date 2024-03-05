#!/usr/bin/python3
"""FileStorage class module"""

import json


class FileStorage():
    """Creates a file storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_storage = {}
        for key, value in self.__objects.items():
            dict_storage[key] = value.to_dict()
        
        with open(self.__file_path, "w",) as f:
            json.dump(dict_storage, f)

    def reload(self):
        """Deserializes the JSON file to __objects if only it exists"""
        with open(self.__file_path, "r") as f:
            loaded_storage = json.load(f)
            









