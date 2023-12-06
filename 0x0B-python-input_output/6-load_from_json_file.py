#!/usr/bin/python3
"""

Defines load_from_json_file function.

"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): path to the file
    """
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
