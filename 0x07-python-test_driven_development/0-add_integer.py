#!/usr/bin/python3
""" function adds two integers """

def add_integer(a, b=98):
    """
    a and b must be integers or floats
    otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer
    Returns an integer: the addition of a and b
    """
    if (not(isinstance(a, int)
            or isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not(isinstance(b, int)
            or isinstance(b, float))):
        raise TypeError("b must be an integer")

    """ Cast inputs to integers if they are floats """
    return (int(a) + int(b))
