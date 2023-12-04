#!/usr/bin/python3
"""Module implementing function to determine subclass membership"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise, False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a class that inherited from a_class;
    otherwise, False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
