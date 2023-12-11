#!/usr/bin/python3

"""

Module for Square class.

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Notes:
        width and height are equal to size in a square.

    Attributes:
        width (int): width of the square.
        height (int): height of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor

        Args:
            size (int): size of the square.
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representing the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of the square

        Args:
            *args (ints): New attribute values.
                - 1st argument: id attribute
                - 2nd argument: size attribute
                - 3rd argument: x attribute
                - 4th argument: y attribute
            **kwargs (dict): key/value pairs of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
