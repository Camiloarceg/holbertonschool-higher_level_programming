#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            boolean_list[i] = True
        else:
            boolean_list[i] = False
    return boolean_list
