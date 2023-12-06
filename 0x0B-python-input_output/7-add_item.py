#!/usr/bin/python3

"""

Defines a function that adds all arguments to a Python list,
    and then save them to a file.

"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """Adds all arguments to a Python list, and then save them to a file.

    Args:
            args (list): list of arguments
    """
    my_list = []
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    finally:
        my_list.extend(args)
        save_to_json_file(my_list, "add_item.json")
