#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """class Square that defines a square

    Attributes:
        __size (int): positive integer.
        __position (tuple): position of the square.
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """ Init a new square.

        Args:
            size (int): size of the new square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        if ((not isinstance(position, tuple)) or len(position) != 2 or
            (not isinstance(position[0], int)) or (not isinstance(position[1], int)) or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self) -> tuple:
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value: tuple) -> None:
        if ((not isinstance(value, tuple)) or len(value) != 2 or
            (not isinstance(value[0], int)) or value[0] < 0 or
                (not isinstance(value[1], int)) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def my_print(self) -> None:
        """Print the square with the character #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print("")
