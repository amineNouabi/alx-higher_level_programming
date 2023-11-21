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
        self.size(size)

    def size(self) -> int:
        """Get the size of the square"""
        return self.__size

    def size(self, value: int) -> None:
        """Set the size of the square

        Args:
            value (int): new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self) -> int:
        """Calculates the area of a square

        Returns:
            The area of the square

        """
        return self.__size ** 2
