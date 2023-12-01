#!/usr/bin/python3

"""

Module defining text_indentation function

"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
            text (str): text to print

    Raises:
            TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    print(text, end="")
