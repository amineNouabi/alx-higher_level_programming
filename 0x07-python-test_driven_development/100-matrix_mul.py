#!/usr/bin/python3

"""

Module defining matrix_mul function

"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices

    Args:
        m_a (nuber[][]): matrix a
        m_b (nuber[][]): matrix b

    Raises:
        TypeError: m_a must be a list
        TypeError: m_b must be a list
        TypeError: m_a must be a list of lists
        TypeError: m_b must be a list of lists
        ValueError: m_a can't be empty
        ValueError: m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size
        TypeError: each row of m_b must be of the same size
        ValueError: m_a and m_b can't be multiplied
    """

    m_c = []

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        for cell in row:
            if not isinstance(cell, int) and not isinstance(cell, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        for cell in row:
            if not isinstance(cell, int) and not isinstance(cell, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(len(m_a)):
        m_c.append([])
        for j in range(len(m_b[0])):
            m_c[i].append(0)
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
