#!/usr/bin/python3
"""

Defines Rectangle class.

"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle.

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
        __x (int): x coordinate of rectangle
        __y (int): y coordinate of rectangle
        id (int): object ID

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
            id (int): object ID

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y is negative.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
             int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the rectangle.

        Returns:
            int: The x coordinate of the rectangle.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the rectangle.

        Args:
            value (int): The x coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the rectangle.

        Returns:
            int: The y coordinate of the rectangle.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle.

        Args:
            value (int): The y coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self) -> None:
        """Prints the rectangle using the # character."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Updates the rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument: id attribute
                - 2nd argument: width attribute
                - 3rd argument: height attribute
                - 4th argument: x attribute
                - 5th argument: y attribute
            **kwargs (dict): key/value pairs of attributes.

        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, attr in enumerate(args):
                setattr(self, attrs[i], attr)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
