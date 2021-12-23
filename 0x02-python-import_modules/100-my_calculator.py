#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

from sys import argv


def main():
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = argv[1]
    operator = argv[2]
    b = argv[3]
    operators = ['+', '-', '*', '/']
    functions = [add(int(a), int(b)), sub(int(a),
                 int(b)), mul(int(a), int(b)), div(int(a), int(b))]

    for i in range(len(operators)):
        if operator == operators[i]:
            result = functions[i]
            print('{} {} {} = {}'.format(a, operator, b, result))
            break

    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)


if __name__ == "__main__":
    main()
