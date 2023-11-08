#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operations = {
        "+": add,
        "-": sub,
        "/": div,
        "*": mul
    }
    n = len(sys.argv)

    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, op, b, operations[op](a, b)))
