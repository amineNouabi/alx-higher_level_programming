#!/usr/bin/python3
"""

Module defines MyInt class

"""


class MyInt(int):
    """
    Class MyInt inherits from int
    """

    def __eq__(self, other):
        """
        Returns True if not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Returns True if equal
        """
        return super().__eq__(other)
