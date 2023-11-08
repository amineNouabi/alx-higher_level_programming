#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 2:
        print("{} arguments:".format(n - 1))
    else:
        print("{} argument:".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
