#!/usr/bin/python3
"""Square representation."""


class Square:
    """A class to define square."""

    def __init__(self, size):
        """Initialization of the square.
        Attributes:
            size: size of the square.
        """
        self.size = size

    @property
    def size(self):
        """set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print square with #."""
        for i in range(0, self.__size):
            [print('#', end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
