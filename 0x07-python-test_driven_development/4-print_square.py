#!/usr/bin/python3
""" Module with a funtion that prints a square """


def print_square(size):
    """ It's a function that prints a square with the character #.

    Args:
        size (int): the dimentions of the square.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(0, size):
        print('#' * size)
