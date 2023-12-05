#!/usr/bin/python3
"""Module to append text to a file"""

def append_write(filename="", text=""):
    """appends a string at the end of a text file.

    Args:
    filename = the file name
    text = the text to append

    Returns:
    the number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
