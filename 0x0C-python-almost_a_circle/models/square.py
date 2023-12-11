#!/usr/bin/python3
"""
This class create a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class representaation of a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialising Data
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        return size value
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        update the size value
        """
        self.data_validator("width", size)
        self.width = size
        self.height = size

    def data_validator(self, attribute, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"{attribute} must be a number")
        if value <= 0:
            raise ValueError(f"{attribute} must be greater than zero")

    def __str__(self):
        """
        returns a string with the chars of the square
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        updates attributes of the square
        """
        arg_list = ["id", "size", "x", "y", "\0"]
        if (len(args)):
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns the dictionary representation of square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}