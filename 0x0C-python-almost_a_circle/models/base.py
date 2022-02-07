#!/usr/bin/python3
""" Module with the base class """
import json


class Base:
    """ Base class for the project almost a circle """

    __nb_objects = 0
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        the_file = '{}.json'.format(cls.__name__)
        dictionary = []
        if list_objs is not None:
            for i in list_objs:
                dictionary.append(cls.to_dictionary(i))

        with open(the_file, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(dictionary))
