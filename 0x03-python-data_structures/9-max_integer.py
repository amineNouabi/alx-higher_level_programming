#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for i in my_list:
        if not max or i > max:
            max = i
    return max
