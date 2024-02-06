#!/usr/bin/python3

"""

Defines a class Student.

"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): a list of attributes

        Returns:
            dict: a dictionary containing only the keys listed in attrs

        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
