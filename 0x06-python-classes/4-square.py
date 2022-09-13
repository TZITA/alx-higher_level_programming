#!/usr/bin/python3
"""Square representation."""


class Square:
    """A class that defines square."""

    def __init__(self, size=0):
        """Initialization of a square.
        Attributes:
            size: size of the square.
        """
        self.size = size

    @property
    def size(self):
        """set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)
