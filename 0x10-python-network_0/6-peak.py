#!/usr/bin/python3
"""Module defining find_peak Funtion"""


def find_peak(list_of_integers, start=None, end=None):
    """Find a peak in a list of unsorted integers"""
    if start is None or end is None:
        start, end = 0, len(list_of_integers) - 1
    if start == end:
        return list_of_integers[start]
    if end == start + 1:
        return max(list_of_integers[start], list_of_integers[end])

    middle = (start + end) // 2
    if list_of_integers[middle - 1] > list_of_integers[middle]:
        return find_peak(list_of_integers, start, middle - 1)
    elif middle + 1 <= end and \
            list_of_integers[middle + 1] > list_of_integers[middle]:
        return find_peak(list_of_integers, middle + 1, end)
    else:
        return list_of_integers[middle]
