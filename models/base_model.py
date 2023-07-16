#!/usr/bin/python3
"""Module that declares and defines the 'BaseModel' class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class 'BaseModel' declaration and definition"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.\
                            strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    continue
                self.__dict__[key] = kwargs[key]

    def __str__(self):
        """String representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update 'updated_at' field attribute with
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method that returns dictionary containing all
        key/ values of '__dict__' of the instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
