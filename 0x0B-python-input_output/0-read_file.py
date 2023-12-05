#!/usr/bin/python3
"""Module of a function that reads a text file"""

def read_file(filename=""):
   """read element to the file

    Args:
        filename: the file name
    """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end='')
