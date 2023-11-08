#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [elem**2 for elem in row], matrix))
