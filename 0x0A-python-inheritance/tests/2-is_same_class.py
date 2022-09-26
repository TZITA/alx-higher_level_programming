#!/usr/bin/python3
"""Defines a function is same class."""


def is_same_class(obj, a_class):
    """Returns TRUE if an instance of the class ; otherwise False.

    Args:
        1. obj: The object to be checked.
        2. a_class: The class that will be checked against.
    Returns:
        True - if the object isan instance of the specified class
        False - the object is not an instance of the specified class
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
