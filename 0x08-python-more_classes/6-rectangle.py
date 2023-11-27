#!/usr/bin/python3
"""
This module contains an empty class that defines a rectangle.
"""


class Rectangle:
    """an empty class Rectangle that defines a rectangle
    a rectangle is a parallelogram with four right angles
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        instantiates a rectangle with private instance attributes
        height and width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        this public instance method returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        this public instance method returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        """
        returns a string that is rectangle using hash characters and newlines
        """
        string = ""
        if self.width > 0 and self.height > 0:
            string = "".join(('#' * self.width + '\n') * self.height)
            string = string[:-1]
        return string

    def __repr__(self):
        """
        returns a string representation of the rectangle that allows
        creation of a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        prints a string when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
