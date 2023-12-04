#!/usr/bin/python3
"""Module implementing function to determine subclass membership"""

def inherits_from(obj, a_class):
    """check if it inherited instance of that class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
