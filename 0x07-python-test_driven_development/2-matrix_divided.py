#!/usr/bin/python3
""" Module with just a funtion that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix.

    Args:
        matrix (int or floats): matrix must be
        a list of lists of integers or floats.
        div (int or float): div must be a number (integer or float).

    Returns:
        int or float: Returns a new matrix.
    """
    count = 0
    new_matrix = []
    msg = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in range(0, len(matrix)):
        new_matrix.append([])
        if count == 0:
            actual_row = len(matrix[row])
        else:
            last_row = actual_row
            actual_row = len(matrix[row])
            if not last_row == actual_row:
                raise (
                    TypeError
                    ('Each row of the matrix must have the same size'))
        count += 1

        for number in range(0, len(matrix[row])):
            if not isinstance(matrix[row][number], (int, float)):
                raise TypeError(msg)
            result = round(matrix[row][number] / div, 2)
            new_matrix[row].append(result)

    return new_matrix
