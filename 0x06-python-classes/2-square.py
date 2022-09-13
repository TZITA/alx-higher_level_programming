#!/usr/bin/python3
"""A class that defines square."""


class Square:
    """Square representation."""
    

    def __init__(self, size=0):
        """Initialization of a square.
        Attributes:
            size: Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
