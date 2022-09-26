#!/usr/bin/python3
"""Defines a class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialization of rectangle.

        Args:
            1. width: Width of the rectangle.
            2. height: Height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return print and str rep of a rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
