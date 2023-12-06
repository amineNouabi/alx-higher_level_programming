#!/bin/usr/python3
"""

Defines save_to_json_file function

"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): object to be serialized
        filename (str): path to the file
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
