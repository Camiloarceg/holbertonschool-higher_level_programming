#!/usr/bin/python3

import hidden_4


def run():

    o_hidden_4 = dir()
    for i in range(0, len(o_hidden_4)):
        if not o_hidden_4[i][0:2] == "__":
            print("{}".format(o_hidden_4[i]))

if __name__ == "__main__":
    run()