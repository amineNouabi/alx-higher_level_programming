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
        if not isinstance(position, tuple) or len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        """Get the size of the square"""
        return (self.__size)

    @size.setter
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

    @property
    def position(self) -> tuple:
        """Get the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value: tuple) -> None:
        """Set the position of the square

        Args:
            value (tuple): new position of the square.

        """
        if not isinstance(value, tuple) or len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """Calculates the area of a square

        Returns:
            The area of the square

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.__position[0]):
                print("_", end="")
            print("#" * self.size)
