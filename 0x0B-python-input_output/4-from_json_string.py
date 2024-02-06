#!/usr/bin/python3

"""

Module defining from_json_string function.

"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): JSON string representation of an object
    """
    import json
    return json.loads(my_str)
