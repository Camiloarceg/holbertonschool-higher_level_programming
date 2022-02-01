#!/usr/bin/python3
""" a function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ the funtion in the module """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        charcount = myFile.write(text)
        return charcount
