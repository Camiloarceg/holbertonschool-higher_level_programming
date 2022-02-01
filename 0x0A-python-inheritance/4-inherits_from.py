#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited (directly
or indirectly) from the specified class, otherwise return False.
"""


def inherits_from(obj, a_class):
    """ Function for attributes """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
