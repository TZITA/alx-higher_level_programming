#!/usr/bin/python3
"""Defines a function that checks class and inherited class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is instance of a class or inherited class.

    Args:
        1. obj: The object to be checked.
        2. a_class: The class that the obj is going to be checked against
    Returns:
        True - if obj is instance of a class or inherited class
        False - otherwise
    """
    if isinstance(obj, a_class) is True:
        return (True)
    return (False)
