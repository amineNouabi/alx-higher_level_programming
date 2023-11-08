#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for key in a_dictionary.keys():
        if value == a_dictionary[key]:
            to_delete.append(key)
    for key in to_delete:
        a_dictionary.pop(key)
    return a_dictionary
