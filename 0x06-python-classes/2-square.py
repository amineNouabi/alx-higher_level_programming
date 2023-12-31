#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """ Init a new square.

        Args:
            size (int): size of the new square defaults to 0.

        Raises:
            TypeError: size must be integer.
            ValueError: size must be >= 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
