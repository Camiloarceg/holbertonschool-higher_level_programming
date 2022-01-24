#!/usr/bin/python3
""" Module with a class rectangle """


class Rectangle:
    """ A rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Rectangle constructor.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ area calculation for the rectangle """

        return self.width * self.height

    def perimeter(self):
        """ perimeter calculation for the rectangle """

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ generates a string printable of the rectangle """

        rectangle = ''

        if self.width == 0 or self.height == 0:
            return rectangle
        rectangle = (((self.width * str(self.print_symbol)) + '\n')
                     * self.height)
        return rectangle[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle """

        return ('Rectangle({}, {})'.format(self.width, self.height))

    def __del__(self):
        """ displays a message when a object is deleted """

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
