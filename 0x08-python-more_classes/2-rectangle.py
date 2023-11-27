#!/usr/bin/python3
"""Module for a class Rectangle that defines a rectangle"""
class Rectangle():
    def __init__(self, width=0, height=0):
        """Instantiation of rectangle with `width` and `height`"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for `width` attribute.

        Returns: value of `width` attribute.
        """
        return self.__width

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
        """Getter function for `height` attribute.

        Returns: value of `height` attribute.
        """
        return self.__height

    """Setter for `height` attribute"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the are of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
