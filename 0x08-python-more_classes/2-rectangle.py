#!/usr/bin/python3
"""

Module defining Rectangle Class

"""


class Rectangle:
    """Rectangle Class Definition

    Arguments:
        __height (int): Rectangle height.
        __width (int): Rectangle width.
    """

    def __init__(self, width=0, height=0):
        """Initilize a new rectangle

        Args:
            width (int, optional): width of new rectagle. Defaults to 0.
            height (int, optional): height of new rectangle. Defaults to 0.

        Raises:
            TypeError: if height or width is not an integer.
            ValueError: if height or width is smaller than 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width proprety"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value (int): new width

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is smaller than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height proprety"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Args:
            value (int): new height.

        Raises:
            TypeError: if height is not an integer or smaller than 0.
            ValueError: if height is smaller than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates Rectangle area.

          Returns:
              Area of the square self.
        """
        return (self.height * self.width)

    def perimeter(self):
        """Calculates Rectangle Perimeter.

          Returns:
              Perimeter of the square self.
        """
        if not self.height or not self.width:
            return (0)
        return (2 * (self.height + self.width))
