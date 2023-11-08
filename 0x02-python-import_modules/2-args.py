#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    print("{} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, sys.argv[i]))
