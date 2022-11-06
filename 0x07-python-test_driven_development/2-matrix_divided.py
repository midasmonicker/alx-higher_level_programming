#!/usr/bin/python3
"""Function that divides all elements  of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides the integers & floats of a matrix
    Args:
        matrix: list of lists of integers/floats
        div: divisor for the numbers in the matrix
    Returns: A new matrix with the result after division
    Raises:
        TypeError:  If the elements of the matrix are not lists
                    If the elements of the lists are not integers/floats
                    If div is not an integer/float
                    If the lists of the matrix dont have the same size
        ZeroDivisionError: If div is zero
        """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    len_elem = 0
    row_size = "Each row of the matrix must have the same size"

    for elem in matrix:
        if not elem or not isinstance(matrix, list):
            raise TypeError(error_msg)

        if len_elem != 0 and len(elem) != len_elem:
            raise TypeError(row_size)

        for num in elem:
            if not isinstance(num, (int, float)):
                raise TypeError(error_msg)

        len_elem = len(elem)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
