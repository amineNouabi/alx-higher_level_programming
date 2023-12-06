#!/usr/bin/python3
"""

Defines a function that inserts a line of text to a file,
    after each line containing a specific string.

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
            after each line containing a specific string.

    Args:
        filename (str, optional): path to the file. Defaults to "".
        search_string (str, optional): string to search for in the file.
                Defaults to "".
        new_string (str, optional): string to insert. Defaults to "".
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.writelines(lines)
