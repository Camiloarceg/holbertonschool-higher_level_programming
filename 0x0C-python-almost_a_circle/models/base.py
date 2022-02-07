#!/usr/bin/python3
""" Module with the base class """
import json


class Base:
    """ Base class for the project almost a circle """

    __nb_objects = 0
    def __init__(self, id=None):

        """ The Class constructor for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method for convert python obj to json """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        the_file = '{}.json'.format(cls.__name__)
        dictionary = []
        if list_objs is not None:
            for i in list_objs:
                dictionary.append(cls.to_dictionary(i))

        with open(the_file, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """
        file_name = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(file_name, mode="r", encoding="utf-8") as myFile:
                json_file = myFile.read()
        except FileNotFoundError:
            return instances
        python_objs = cls.from_json_string(json_file)
        for obj in python_objs:
            instances.append(cls.create(**obj))
        return instances
