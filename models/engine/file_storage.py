#!/usr/bin/python3
"""FileStorage class module"""

import json
import os


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
        from models import base_model
        from models import user
        from models import state
        from models import city
        from models import amenity
        from models import place
        from models import review

        global dict_module
        dict_module = {'BaseModel': base_model,
                       'User': user,
                       'State': state,
                       'City': city,
                       'Amenity': amenity,
                       'Place': place,
                       'Review': review
                       }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                loaded_storage = json.load(f)

            for key, dict_attr in loaded_storage.items():
                try:
                    class_name = dict_attr['__class__']
                except TypeError:
                    continue
                if class_name in dict_module:
                    get_module = dict_module[class_name]

                new_model = getattr(get_module, class_name)

                self.__objects[key] = new_model(**dict_attr)
