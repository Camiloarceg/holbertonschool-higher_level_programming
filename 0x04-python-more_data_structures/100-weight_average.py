#!/usr/bin/python3


def weight_average(my_list=[]):
    weight = 0
    score = 0
    if my_list:
        for i in my_list:
            weight += i[1]
            score += i[0] * i[1]
        return score / weight
    return 0
