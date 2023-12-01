#!/usr/bin/python3
"""

Module defining matrix divide element wise function

"""


def matrix_divided(matrix, div):
    """Divide Matrix element wise

    Args:
        matrix (int[][] or float[][]): numeric matrix
        div (int or float): number to divide by

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    matrix_type_error = "matrix must be"
    matrix_type_error += " a matrix (list of lists) of integers/floats"
    length = 0
    m = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_type_error)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_type_error)
        if length == 0:
            length = len(row)
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for cell in row:
            if not isinstance(cell, int) and not isinstance(cell, float):
                raise TypeError(matrix_type_error)
            new_row.append(round(cell / div, 2))
        m.append(new_row)
    return m
