#!/usr/bin/python3

"""

Defines Base class.

"""


class Base:
    """Represents a base.

    Attributes:
        __nb_objects (int): total number of objects
        id (int): object ID

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): object ID
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
