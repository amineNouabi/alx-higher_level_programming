#!/usr/bin/python3

"""

Module defines is_kind_of_class function

"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an
    instance of the specified class of a class that inherited from,
    the specified class otherwise False.
    """
    return isinstance(obj, a_class)
