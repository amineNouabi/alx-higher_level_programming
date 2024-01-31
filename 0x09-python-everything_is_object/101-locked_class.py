#!/usr/bin/python3
"""

Module defining LockedClass Class.

"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes.
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        Prevents the user from dynamically creating new instance attribute beside 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
