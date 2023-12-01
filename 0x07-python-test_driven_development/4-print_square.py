#!/usr/bin/python3

"""

Module defining print_square function

"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size for i in range(size)]))
