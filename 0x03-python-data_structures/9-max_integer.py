#!/usr/bin/python3


def max_integer(my_list=[]):
    max_num = 0
    if my_list:
        for num in my_list:
            if num >= max_num:
                max_num = num
    else:
        return None
    return max_num
