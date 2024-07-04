#!/usr/bin/python3
"""Module defining find_peak Funtion"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not len(list_of_integers):
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return
    middle = n // 2

    if list_of_integers[middle - 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[:middle])
    elif list_of_integers[middle + 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[middle:])
    return list_of_integers[middle]
