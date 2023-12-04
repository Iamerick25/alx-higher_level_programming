#!/usr/bin/python3
"""Module of a fuction to check kinds of class"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class or its
    subclasses; otherwise, False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or its subclasses; otherwise, False.
    """
    return (isinstance(obj, a_class))
