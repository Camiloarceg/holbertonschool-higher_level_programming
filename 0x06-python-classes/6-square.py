#!/usr/bin/python3
"""defines a square by: (based on 4-square.py)"""


class Square:
    """Square class with an constructor"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor for the class Square

        Args:
            size (int): The size of a square
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """ prints in stdout the square with the character #"""

        if self.size is 0:
            print()
        else:
            for i in range(1, self.size+1):
                for j in range(1, self.size+1):
                    print("#", end="")
                print()

    @property
    def position(self):

        """getter for position

        Returns:
            int: the position od the square
        """

        return self.__position

    @position.setter
    def position(self, value):

        """setter for position

        Raises:
            TypeError: position must be a tuple of 2 positive integers
            TypeError: position must be a tuple of 2 positive integers
            TypeError: position must be a tuple of 2 positive integers
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value
