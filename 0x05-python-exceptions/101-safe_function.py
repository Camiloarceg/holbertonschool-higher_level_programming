#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)

    except (ValueError, TypeError, ZeroDivisionError, IndexError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
