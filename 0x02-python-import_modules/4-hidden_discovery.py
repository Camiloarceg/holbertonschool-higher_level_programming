#!/usr/bin/python3

import hidden_4


def run():

    for i in dir(hidden_4):
        if i.startswith("__") is False:
            print(i)

if __name__ == "__main__":
    run()