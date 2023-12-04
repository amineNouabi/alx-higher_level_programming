#!/usr/bin/python3
"""

Module defines lookup function

"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
