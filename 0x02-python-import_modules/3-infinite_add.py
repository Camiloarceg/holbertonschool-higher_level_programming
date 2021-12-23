#!/usr/bin/python3

from sys import argv


def main():
    add = 0
    length = len(argv) - 1
    if length == 0:
        print('{}'.format(add))
    else:
        for i in range(1, length + 1):
            add += int(argv[i])
        print('{}'.format(add))


if __name__ == '__main__':
    main()
