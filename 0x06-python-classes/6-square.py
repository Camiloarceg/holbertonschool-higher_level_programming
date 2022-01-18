#!/usr/bin/python3
""" Square Class """


class Square:

    """ Defines a square
    Args:
        size (int) = Size of the square
        position (tuple) = Position of the square
    - If size is not an integer, raise a TypeError exception
      with the message: "size must be an integer"
    - If size is less than 0, raise a ValueError exception
      with the message: "size must be >= 0"
    """

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

    def area(self):

        """ Returns the current square area """

        return (self.__size ** 2)

    def my_print(self):

        """ Prints in stdout the square with the character '#' """

        if self.size > 0:

            if self.position[1] > 0:
                print("\n" * self.position[1], end="")

            for i in range(self.size):

                print(" " * self.position[0], end="")
                print("#" * self.size)

        else:
            print()

    @property
    def size(self):

        """ Retrieve the property value """

        return self.__size

    @size.setter
    def size(self, value):

        """ Set the property value """

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):

        """ Retrieve the property value """

        return self.__position

    @position.setter
    def position(self, value):

        """ Set the property value """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value
