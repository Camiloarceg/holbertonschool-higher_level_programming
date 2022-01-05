#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletes = []
    if a_dictionary:
        for key, value_d in a_dictionary.items():
            if value_d == value:
                deletes.append(key)
        if deletes:
            for i in deletes:
                del a_dictionary[i]
    return a_dictionary
