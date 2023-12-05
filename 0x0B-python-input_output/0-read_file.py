#!/usr/bin/python3
"""Module of a function that reads a text file"""

def read_file(filename=""):
    """Reads a UTF8 file and prints to STDOUT"""

    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end='')
