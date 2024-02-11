#!/usr/bin/python3
"""
Defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in this project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list (not used).
            **kwargs: Arbitrary keyword arguments.
                If provided, set attributes according to the key/value pairs
                in kwargs.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
