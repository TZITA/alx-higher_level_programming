#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Initialization of the class."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            1. name: Name
            2. value: Value associated with the name.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name)) 
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
