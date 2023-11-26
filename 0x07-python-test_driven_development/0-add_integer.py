#!/usr/bin/python3
"""Module defining a 2 numbers addition function"""


def add_integer(a, b=98):
    """Returns integer addition of two numbers

    Args:
        a (int or float): first number
        b (int or float, optional): second number. Defaults to 98.

    Raises:
        TypeError: If a or b is not a number (int or float)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
