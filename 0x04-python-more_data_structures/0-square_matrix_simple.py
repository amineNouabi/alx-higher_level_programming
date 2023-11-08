#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for row in matrix:
        m.append([i**2 for i in row])
    return m
