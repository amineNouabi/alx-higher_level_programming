#!/usr/bin/python3

"""

Module defining say_my_name function

"""


def say_my_name(first_name, last_name=""):
    """Prints a string with first and last name

    Args:
            first_name (str): first name
            last_name (str, optional): last name

    Raises:
            TypeError: first_name must be a string
            TypeError: last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
