#!/usr/bin/python3
"""Defines a class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialization of the subclass Rectangle.

        Args:
            1. width: Width of the rectangle
            2. height: Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
