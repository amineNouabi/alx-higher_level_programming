#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Empty class Square that defines a square"""

    def __init__(self, size=0) -> None:
        """Initializes the data"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
