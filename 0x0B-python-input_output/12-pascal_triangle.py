#!/usr/bin/python3
""" This module contains a triangle pascal """


def pascal_triangle(n):
    """ asfsfasgdsgdgs efsgwsegs """

    if n <= 0:
        return list =[]
    list = []
    for nivel in range(n):
        list.append([])
        for j in range(nivel, -1, -1):
            valor = factorial(nivel)/(factorial(j)*factorial(nivel-j))
            list[nivel].append(int(valor))
    return list


def factorial(n):

    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
