#!/usr/bin/python3

def islower(c):
    if ord(c) <= ord("z") and ord(c) >= ord("a"):
        return True
    return False


def uppercase(s):
    delta = ord('a') - ord('A')
    for ch in s:
        to_to = ch
        if islower(ch):
            to_to = chr(ord(ch) - delta)
        print("{}".format(to_to), end="")
    print("".format())
