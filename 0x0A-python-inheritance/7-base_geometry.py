#!/usr/bin/python3
"""

Module defines BaseGeometry class

"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Raises an Exception with the message:
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates numeric value.

        Args:
            name (str): name of value.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
