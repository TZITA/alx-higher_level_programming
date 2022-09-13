#!/usr/bin/python3
"""Square representation."""


class Square:
    """A class that define a square."""

    def __init__(self, size=0):
        """Initializing a square.
           Attributes:
           size: size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area."""
        return (self.__size * self.__size)
