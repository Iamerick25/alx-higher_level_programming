#!/usr/bin/python3
"""Function of a class Rectangle that defines a rectangle"""



class Rectangle():
    """definition of class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instatiation of a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    """Setter function for `width` attribute"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    """Setter function for `height` attribute"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
