#!/usr/bin/python3
"""Defines a rectangle class that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle inheriting from Class Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class rectangle.
        Args:
            1. width: Width of the rectangle.
            2. height: Height of the rectangle.
            3. x: x coordinate of the rectangle.
            4. y: y coordinate of the rectangle.
            5. id: id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Gets the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle."""
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Gets x coordinate of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets x coordinate of the rectangle."""
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Gets y coordinate of the rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets y coordinate of the rectangle."""
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range(self.height):
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """String rep of the rectangle object."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
