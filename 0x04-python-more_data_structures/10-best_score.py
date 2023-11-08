#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = None
    max = None
    for key in a_dictionary:
        if not max_key and not max or max < a_dictionary[key]:
            max_key = key
            max = a_dictionary[key]
    return max_key
