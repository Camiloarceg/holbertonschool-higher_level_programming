#!/usr/bin/python3
""" a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ funtion to append in the module """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        charcount = myFile.write(text)
        return charcount
