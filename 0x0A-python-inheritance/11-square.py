#!/usr/bin/python3
"""Defines a class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass square inherits from class rectangle."""

    def __init__(self, size):
        """Initialization of a square.

        Args:
            1. size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
