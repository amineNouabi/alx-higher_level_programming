#!/usr/bin/python3

"""

Module defining text_indentation function

"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): text to print.

    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip(" ")
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in ".?:" or text[i] == "\n":
            if text[i] in ".?:":
                new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(new_text, end="")
