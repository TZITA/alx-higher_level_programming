#!/usr/bin/python3
"""Defines a function that adds an attribute to an object."""



def add_attribute(obj, atr, value):
    """Adds a new attribute to an obj.
    Args:
        1. obj: Object.
        2. atr: attribute to be added.
        3. value: the value of atr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
