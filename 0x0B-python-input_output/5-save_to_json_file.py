#!/usr/bin/python3
"""Module writes an Object to a text file"""

import json

def save_to_json_file(my_obj, filename):
    """using a JSON representation to save a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
