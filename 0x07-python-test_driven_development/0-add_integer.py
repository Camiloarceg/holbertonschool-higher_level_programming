#!/usr/bin/python3
"""Module with only a funtion that adds 2 integres"""


def add_integer(a, b=98):
    """adds 2 integres

    Args:
        a (int): first int.
        b (int): second int. Defaults to 98.
    Returns:
        the add between a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a + b)
