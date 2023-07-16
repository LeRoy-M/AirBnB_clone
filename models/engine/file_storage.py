#!/usr/bin/python3
"""Module that declares and defines the 'FileStorage' class"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """Class 'FileStorage' declaration and definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Method that sets 'obj' in '__object' with
        key '<obj class name>.id'
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Method that serializes '__objects' to a JSON file"""
        temp = {key: FileStorage.__objects[key].to_dict() for key in
                FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, mode='w') as po:
            json.dump(temp, po)

    def reload(self):
        """Method that deserialzies a JSON file to '__objects'"""
        if not path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, mode='r') as js:
                FileStorage.__objects = json.load(js)
        except json.decoder.JSONDecodeError:
            pass
