#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class"""

    state_id: str = ""
    name: str = ""
