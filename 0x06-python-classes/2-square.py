#!/usr/bin/python3
"""The square module continue"""

class Square:
"""The class to create square."""

    def __init__(self, size=0):
        """set size to private instance variable"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
