#!/usr/bin/python3

def remove_char_at(s, i):
    if i < 0:
        return s
    return "{}{}".format(s[:i], s[i + 1:])
