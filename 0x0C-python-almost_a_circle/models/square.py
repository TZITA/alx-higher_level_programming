#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A sub class square that inherits from the class rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the class square.
        Args:
            1. size: The length of the square.
            2. x: x coordinate.
            3. y: y coordinate.
            4. id: id of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def __str__(self):
        """Str rep of a square obj."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
