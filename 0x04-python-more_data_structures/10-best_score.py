#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary)
        max_val = a_dictionary[keys[0]]
        for key in keys:
            if a_dictionary[key] >= max_val:
                max_key = key
                return max_key
    else:
        return None
