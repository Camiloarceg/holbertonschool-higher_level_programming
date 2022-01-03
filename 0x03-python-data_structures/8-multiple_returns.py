#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        the_tuple = (len(sentence), sentence[0])
    else:
        the_tuple = (0, None)
    return the_tuple
