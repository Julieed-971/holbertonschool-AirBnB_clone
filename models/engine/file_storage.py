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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_storage = {}
        for key, value in FileStorage.__objects.items():
            dict_storage[key] = value.to_dict()

        with open(self.__file_path, "w",) as f:
            json.dump(dict_storage, f)

    def reload(self):
        """Deserializes the JSON file to __objects if only it exists"""
        from models import base_model

        # Dictionary mapping class names to their corresponding module
        global dict_module
        dict_module = {'BaseModel': base_model}

        # Load the contents of the JSON file into loaded_storage
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                loaded_storage = json.load(f)

            # Iterate through loaded storage to get the attributes list
            for key, dict_attr in loaded_storage.items():
                # Get the class name
                class_name = dict_attr['__class__']

                # Retrieve the corresponding module
                if class_name in dict_module:
                    get_module = dict_module[class_name]

                # Retrieve the class object corresponding to
                # the class name from the module
                new_model = getattr(get_module, class_name)

                # Instantiate the class object with attributes
                # extracted from the JSON data and
                # store the instance in __objects
                FileStorage.__objects[key] = new_model(**dict_attr)
