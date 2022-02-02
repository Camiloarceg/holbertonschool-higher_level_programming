#!/usr/bin/python3
""" Module with a class student """


class Student():
    """ student class for the project """
    
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(obj):
        return obj.__dict__