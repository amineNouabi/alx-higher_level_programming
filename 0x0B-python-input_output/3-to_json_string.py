#!/usr/bin/python3

"""Defines a function that returns the JSON representation of an object (string). """


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
            my_obj (object): object to be serialized
    """
    import json
    return json.dumps(my_obj)
