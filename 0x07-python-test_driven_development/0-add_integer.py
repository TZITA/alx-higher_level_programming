#!/usr/bin/python3
"""Defines a function to add 2 numbers."""


def add_integer(a, b=98):
    """Function to add integrs a nad b.
    Floats are changed to ints before addition.

    Raises:
        TypeError: If a or b is not integer/float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be integer")
    return (int(a) + int(b))
