#!/usr/bin/python3

def islower(c):
    if ord(c) <= ord("z") and ord(c) >= ord("a"):
        return True
    return False


def uppercase(str):
    delta = ord('a') - ord('A')
    for ch in str:
        to_print = ch
        if islower(ch):
            to_print = chr(ord(ch) - delta)
        print("{}".format(to_print), end="")
    print("".format())
