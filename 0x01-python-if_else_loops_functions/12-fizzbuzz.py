#!/usr/bin/python3

def fizzbuzz():
    for i in range(101):
        if i % 5 and i % 3:
            print("FizzBuzz", end="")
        elif i % 5:
            print("Buzz", end="")
        elif i % 3:
            print("Fizz", end="")
        else:
            print(i, end="")
        if i != 100:
            print(" ", end="")
    print()
