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
        """Base to json string.

        Args:
            list_dictionaries (list): is a list of dictionaries.

        Returns:
            JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return str([str(i) for i in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of objects.
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            list_dictionaries = list(
                map(lambda x: x.to_dictionary(), list_objs))
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 

        Args:
            json_string (string): 
        """
        if json_string is None or not len(json_string):
            return []
        return list(map(lambda object_string: json.loads(object_string.replace("'", "\"")), json.loads(json_string)))