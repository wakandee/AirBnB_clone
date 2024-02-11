#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
import os.path


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_dict = json.load(file)
                from models.base_model import BaseModel  # to avoid circular import

                for key, value in json_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_dict = {k: v for k, v in value.items()}
                    obj_dict["__class__"] = class_name
                    obj = BaseModel(**obj_dict)
                    self.__objects[key] = obj


storage = FileStorage()
storage.reload()
