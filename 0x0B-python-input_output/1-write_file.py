#!/usr/bin/python3

"""Defines a function that writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
        and returns the number of characters written.

    Args:
            filename (str, optional): path to the file . Defaults to "".
            text (str, optional): text to write to the file. Defaults to "".

    Returns:
            int: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
