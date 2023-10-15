#!/usr/bin/python3
"""Defines the amenity class"""

from modes.base_model import BaseModel


class Amenity(BaseModel):
    """
    child class of BaseModel
    has one atrribute - name(empty string)
    """
    name = ""
