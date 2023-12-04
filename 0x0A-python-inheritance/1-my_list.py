#!/usr/bin/python3
"""print sorted list"""


class MyList(list):
    """creates a sorted list"""

    def __init__(self):
        """constructor method"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
