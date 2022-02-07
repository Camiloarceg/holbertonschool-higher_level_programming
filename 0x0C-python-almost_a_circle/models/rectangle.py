#!/usr/bin/python3
""" Module containing the rectangle class """
import json
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method For area calculation """
        area = self.width * self.height
        return area

    def display(self):
        """ Method for displaying the rectangle """
        for ye in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="\n")

    def __str__(self):
        """ Method for the string form of the class """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Method to update the information of an object"""
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg

        else:
            for key, karg in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, karg)

    def to_dictionary(self):
        """ Method to convert object info into a dictionary """
        r_dict = ({'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y})
        return r_dict
