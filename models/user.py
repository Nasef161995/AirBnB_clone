#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ State Class"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
