#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == 101:
        alpha += 1
        continue
    if alpha == 113:
        alpha += 1
        continue
    print('{:c}'.format(alpha), end='')
