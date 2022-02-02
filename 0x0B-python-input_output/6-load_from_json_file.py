#!/usr/bin/python3
""" A module with just one function """
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”
    """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
