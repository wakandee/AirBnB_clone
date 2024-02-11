#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os  # Import the os module
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class to serialize and deserialize instances."""

    CLASSES = {"BaseModel": BaseModel, "User": User}

    def __init__(self):
        """Initialize FileStorage instance."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON."""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserialize JSON to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                deserialized = json.load(file)
            for key, value in deserialized.items():
                cls_name = value["__class__"]
                cls = FileStorage.CLASSES[cls_name]
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
