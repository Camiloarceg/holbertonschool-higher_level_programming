#!/usr/bin/python3
""" Module with a function that says a composed name. """


def say_my_name(first_name, last_name=""):
    """ It's a function that prints My name is <first name> <last name>.

    Args:
        first_name (str): the first name.
        last_name (str, optional): the last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
