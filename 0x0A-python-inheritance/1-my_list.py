#!/usr/bin/python3

"""

Module defines MyList class

"""


class MyList(list):
    """
    Class inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
