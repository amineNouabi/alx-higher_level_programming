#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """class Square that defines a square

    Attributes:
         __size (int): positive integer.

    """

    def __init__(self, size=0) -> None:
        """ Init a new square.

        Args:
            size (int): size of the new square.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Calculates the area of a square

        Returns:
            The area of the square

        """
        return self.__size ** 2
