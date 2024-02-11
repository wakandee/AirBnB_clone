#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))
            if "created_at" not in kwargs:
                setattr(self, "created_at", datetime.now())
            if "updated_at" not in kwargs:
                setattr(self, "updated_at", datetime.now())
        else:
            setattr(self, "id", str(uuid.uuid4()))
            setattr(self, "created_at", datetime.now())
            setattr(self, "updated_at", datetime.now())

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        from models import storage

        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
