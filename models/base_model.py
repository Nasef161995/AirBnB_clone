#!/usr/bin/python3
"""......."""
import uuid
from datetime import datetime


class BaseModel:
    """......."""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # self.name = name
        # self.my_number = my_number
    

    def __str__(self):
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
    
    def save(self):
         self.updated_at = datetime.now()
    
    def to_dict(self):
        new = self.__dict__
        new["__class__"] = self.__class__.__name__
        created_at = created_at.isoformat()
        return new 



a = BaseModel()
print(a)
a.created_at = 10
a.save()

print(a)
