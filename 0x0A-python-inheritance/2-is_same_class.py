#!/usr/bin/python3
"""Module of a fuction to check for same object"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
