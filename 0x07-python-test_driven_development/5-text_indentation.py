#!/usr/bin/python3
""" Module with a function that prints a text with
    2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """ It's a function that prints a text with
        2 new lines after each of these characters: ., ? and :

    Args:
        text (str): the string to be ident.
    """

    initial = final = printed = 0

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    while initial < len(text):
        if text[initial] != " ":
            break

        initial += 1

    final = initial

    for final in range(len(text)):

        printed = 0

        if text[final] == '.' or text[final] == '?' or text[final] == ':':

            final += 1
            print(text[initial:final])
            print()

            while final < len(text):

                if text[final] != " ":
                    break
                final += 1

            initial = final
            printed = 1

    if printed == 0:
        print(text[initial:(final + 1)], end="")
