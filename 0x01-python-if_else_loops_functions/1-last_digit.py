#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = repr(number)[-1]
if number < 0:
    ld = '-' + ld
    ld = int(ld)
else:
    ld = int(ld)
if ld > 5:
    print('Last digit of {:d} is {:d}\
            and is greater than 5'.format(number, ld))
elif lastdigit == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, ld))
else:
    print('Last digit of {:d} is {:d}\
            and is less than 6 and not 0'.format(number, ld))
