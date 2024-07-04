#!/usr/bin/python3
"""Module defining find_peak Funtion"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    middle = n // 2
    if list_of_integers[middle - 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[:middle])
    elif list_of_integers[middle + 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[middle:])
    return list_of_integers[middle]
