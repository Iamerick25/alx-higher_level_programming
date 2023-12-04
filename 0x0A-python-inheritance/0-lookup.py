#!/usr/bin/python3
"""Module of a function that returns the list of available attributes
and methods of an object
"""

def lookup(obj):
    """return available attributes and methods in an object
    """

    return (dir(obj))
