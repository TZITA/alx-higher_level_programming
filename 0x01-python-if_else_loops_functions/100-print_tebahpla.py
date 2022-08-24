#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 == 0:
        print("{}".format(chr(i)), end='')
    else:
        num = i - 32
        print("{}".format(chr(num)), end='')
    i -= 1
