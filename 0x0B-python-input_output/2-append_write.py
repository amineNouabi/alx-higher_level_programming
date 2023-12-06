#!/usr/bin/python3

"""Defines a function that append a string to a text file (UTF8)."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)
        and returns the number of characters written.

    Args:
            filename (str, optional): path to the file . Defaults to "".
            text (str, optional): text to append to the file. Defaults to "".

    Returns:
            int: number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
