#!/usr/bin/python3
"""
this module contains a class MyInt which inherits from int
"""


class MyInt(int):
    """
    this class MyInt inherits from int but has == and != operators inverted
    """
    def __init__(self, value=0):
        """
        instantiates an instance of MyInt with value
        """
        self.__value = value

    def __eq__(self, other):
        """
        inverts == return value
        """
        return self.__value != other

    def __ne__(self, other):
        """
        inverts != return value
        """
        return self.__value == other
