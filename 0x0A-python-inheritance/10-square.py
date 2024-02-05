#!/usr/bin/python3
"""

Module defines Square class

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns area of a square.
        """
        return super().area()
