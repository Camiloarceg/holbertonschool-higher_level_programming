#!/usr/bin/python3
for i in range(97, 123):
    if i == 101:
        i = i + 1
        continue
    if i == 113:
        i = i + 1
        continue
    print("{:c}".format(i), end="")
