#!/usr/bin/python3
i = 97
while i < 123:
    if i == 101 or i == 113:
        print("{}".format(''), end='')
    else:
        print("{}".format(chr(i)), end='')
    i += 1
