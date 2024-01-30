#!/usr/bin/python3
"""

Module defining Rectangle Class

"""


class Rectangle:
    """Rectangle Class Definition

    Attributes:
        height (int): Rectangle height.
        width (int): Rectangle width.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Rectangle to String.

        Returns:
            s: String representation of rectangle using '#' character.
        """
        delimiter = "\n"
        s = ""

        if not self.height or not self.width:
            return (s)
        for i in range(self.height):
            if i == self.height - 1:
                delimiter = ""
            s = "{}{}{}".format(
                s, str(self.print_symbol) * self.width, delimiter)
        return (s)

    def __repr__(self):
        """Rectangle to String that can be used with eval to create objects"""

        str = "Rectangle({}, {})".format(self.width, self.height)
        return str

    def __del__(self):
        """Rectangle Destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter for width proprety"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value (int): new width.

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area.
        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.
        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns new instance of rectangle that satisfies a square.

        Args:
            size (int, optional): size of square. Defaults to 0.
        Returns:
            square: new instance of rectangle that satisfies a square.
        """
        square = Rectangle(size, size)
        return (square)
