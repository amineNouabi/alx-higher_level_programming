#!/usr/bin/python3
"""

Module defining matrix divide element wise function

"""


def matrix_divided(matrix, div):
    """Divide Matrix element wise

    Args:
        matrix (int[][] or float[][]): numeric matrix
        div (int or float): number to divide by
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for cell in row:
            if not isinstance(cell, int) and not isinstance(cell, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
