#!/usr/bin/python3
"""writing the base class"""
import json
import csv


class Base:
    """writing the base class of this model"""

    __nb_objects = 0
    """Class variable representing the total count of Base (and subclass)
    instances.
    """

    def __init__(self, id=None):
        """Initialize new Base instance

        Args:
            id : the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Method to create new instance directly from the class. Mainly
        for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for new instance.

        Returns: New instance of class from which `create` was called.

        Raises: Errors delegated to subclasses of Base which call this
            method.
        """
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        if not hasattr(dictionary, "keys") or not callable(dictionary.keys):
            dictionary = {}
        c.update(**dictionary)
        return c

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to serialize list of dictionary objects into json.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into json
                representation.

        Returns: Json string representation of `list_dictionaries`.

        Raises: Any errors encounterd during serialization.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static method to deserialize json string into python objects.

        Args:
            json_string (str): String representation of objects.

        Returns: Python objects represented by `json_string`.

        Raises: Any errors encountered during serialization.
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Class method to load file containing json serialized objects.
        Attempts to open the file 'class name.json' and deserialize
        it. If it does not exist, returns empty list.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myfile:
                list_dicts = Base.from_json_string(myfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method to convert `list_objs` to csv format and save
        in file with name '<class name>.csv'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any error encounterd during conversion to csv.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Class method to load file containing csv representation of objects.
        Attempts to open the file 'class name.csv' and convert back to
        original list of objects. If it does not exist, returns empty list.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
