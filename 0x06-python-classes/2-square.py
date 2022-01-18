#!/usr/bin/python3
"""defines a square by: (based on 0-square.py)"""


class Square:
    """Square class with an constructor"""
    def __init__(self, size=0):
        """constructor for the class Square

        Args:
            size (int): The size of a square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
