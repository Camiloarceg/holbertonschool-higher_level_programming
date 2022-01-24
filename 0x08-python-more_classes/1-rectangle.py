#!/usr/bin/python3
""" Module with a class rectangle """


class Rectangle:
    """ A rectangle class """
    def __init__(self, width=0, height=0):
        """ Rectangle constructor.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """ getter for height """

        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @property
    def width(self):
        """ getter for width """

        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value
