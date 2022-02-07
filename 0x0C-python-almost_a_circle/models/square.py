#!/usr/bin/python3
""" Module with the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            for key, karg in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, karg)

    def to_dictionary(self):
        s_dict = ({'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y})
        return s_dict
