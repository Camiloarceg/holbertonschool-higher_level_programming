#!/usr/bin/python3
""" module whit a funtion that return the JSON of an string
"""
import json


def to_json_string(my_obj):
    """ From string to JSON
    """

    return json.dumps(my_obj)
