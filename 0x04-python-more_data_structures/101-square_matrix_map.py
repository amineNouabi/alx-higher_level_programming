#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    m = map(lambda row: [elem**2 for elem in row], matrix)
    return list(m)
