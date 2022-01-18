#!/usr/bin/python3
"""defines a square by: (based on 3-square.py)"""


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

    @property
    def size(self):
        """getter for size attribute

        Returns:
            [int]: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size attribute

        Args:
            value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current square area

        Returns:
            [int]: Area of the Square computed
        """
        return self.size * self.size
