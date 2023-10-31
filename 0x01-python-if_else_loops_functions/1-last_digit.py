#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = 1
digit = 0

if number < 0:
    sign = -1
    number *= -1

digit = (number % 10) * sign

print(f'Last digit of { number * sign } is { digit }', end=" ")

if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("is less than 6 and not 0")
