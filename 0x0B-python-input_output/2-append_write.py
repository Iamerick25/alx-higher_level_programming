#!/usr/bin/python3
"""Module to append text to a file"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
    filename (str): file to write to
    text (str): text to write in utf8 encoding

    Returns: number of characters written
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
