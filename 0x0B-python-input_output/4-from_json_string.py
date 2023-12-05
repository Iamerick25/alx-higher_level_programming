#!/usr/bin/python3
"""Module returns an object (Python data structure)"""

import json

def from_json_string(my_str):
    """represented by a JSON string"""
    return (json.loads(my_str))
