#!/usr/bin/python3
"""......."""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects 

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file_json:
            d = {}
            for key, value in FileStorage.__objects.items():
                d[key] = value.to_dict()
            json.dump(d, file_json)
    
    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file_json:
                data = {}
                data = json.load(file_json)
                for value in data.values():
                    self.new(eval(value['__class__'])(**value))
        except:
            pass    
