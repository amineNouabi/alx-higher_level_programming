#!/usr/bin/python3
"""

Defines Base class.

"""

import json


class Base:
    """Represents a base.

    Attributes:
        __nb_objects (int): total number of objects
        id (int): object ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): object ID.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """List of dictionaries to JSON

        Args:
            list_dictionaries (list): is a list of dictionaries.

        Returns:
            JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return str(list_dictionaries).replace("'", "\"")

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of objects.
        """
        filename = cls.__name__ + ".json"
        list_dicts = None
        with open(filename, "w") as file:
            if list_objs is not None:
                list_dicts = list(map(lambda obj: obj.to_dictionary(),
                                      list_objs))
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.

        Args:
            json_string (string): haha.
        """
        if json_string is None or not len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary (dict): key/value pairs of attributes to set.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return list(map(lambda d: cls.create(**d), list_dicts))
        except FileNotFoundError:
            return []
