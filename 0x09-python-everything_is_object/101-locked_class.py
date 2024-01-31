#!/usr/bin/python3
"""

Module defining LockedClass Class.

"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes.
    """

    def __setattr__(self, name, value):
        """Prevents the user from dynamically creating new instance attribute beside 'first_name'.

        Args:
            name (str): name of the attribute.
            value (any): value of the attribute.
        """
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
