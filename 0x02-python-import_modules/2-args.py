#!/usr/bin/python3

from sys import argv


def main():

    length = len(argv) - 1
    if length == 0:
        print('{} arguments.'.format(length))
    elif length == 1:
        print('{} argument:'.format(length))
        print('{}: {}'.format(length, argv[1]))
    else:
        print('{} arguments:'.format(length))
        for i in range(1, length + 1):
            print('{}: {}'.format(i, argv[i]))


if __name__ == "__main__":
    main()
