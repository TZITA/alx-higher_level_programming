#!/usr/bin/python3
"""Defines a function - checks obj is instance of subclass."""


def inherits_from(obj, a_class):
    """Checks obj is instamce of a inherited class.

    Args:
        1. obj: The object to be checke.
        2. a_class: The subclass that obj is going to be checked against.

    Returns:
        True -  if the object is an instance of a class that inherited
        False = otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
         return (True)
    return (False)
