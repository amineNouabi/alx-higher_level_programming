#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    dic = {
        'M': 1000,
        'D':  500,
        'C':  100,
        'L':   50,
        'X':   10,
        'V':    5,
        'I':    1
    }
    sum = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string):
            if dic[roman_string[i]] >= dic[roman_string[i + 1]]:
                sum += dic[roman_string[i]]
                i += 1
            else:
                sum += dic[roman_string[i + 1]] - dic[roman_string[i]]
                i += 2
        else:
            sum += dic[roman_string[i]]
            i += 1
    return sum
