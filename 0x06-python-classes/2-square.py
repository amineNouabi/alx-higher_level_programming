#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Empty class Square that defines a square"""

    def __init__(self, size=0) -> None:
        """Initializes the data"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
