#!/usr/bin/env python3
def no_c(my_string):
    copy = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            copy = "{}{}".format(copy, c)
    return copy
