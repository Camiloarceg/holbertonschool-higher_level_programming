#!/usr/bin/python3
""" This module contains a triangle pascal """


def pascal_triangle(n):
    """ asfsfasgdsgdgs efsgwsegs """

    list = []
    for nivel in range(n):
        list = []
        for j in range(nivel, -1, -1):
            valor = factorial(nivel)/(factorial(j)*factorial(nivel-j))
            list.append(int(valor))
        print(list, end="")
        print()


def factorial(n):

    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


if __name__ == "__main__":
    pascal_triangle(5)
