#!/usr/bin/python3
"""defines a square by: (based on 2-square.py)"""


class Square:
    """Initializes class square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of a square"""
        area = self.__size * self.__size
        return area
