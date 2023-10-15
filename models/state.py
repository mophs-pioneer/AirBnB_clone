#!/usr/bin/python3
"""Defines the state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    child class of BaseModel
    reperesents a state, takes one atrr - name of the state
    """
    name = ""
