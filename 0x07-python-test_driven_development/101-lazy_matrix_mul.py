#!/usr/bin/python3

"""

101-lazy_matrix_mul.py

Module that defines a function that multiplies 2 matrices by using the module NumPy

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy

    Args:
            m_a (list): first matrix
            m_b (list): second matrix

    Returns:
            list: new matrix
    """

    return np.matmul(m_a, m_b)
