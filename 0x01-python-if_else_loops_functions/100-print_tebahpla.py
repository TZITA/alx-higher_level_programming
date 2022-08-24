#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 != 0:
        i = i - 32
        print("{}".format(chr(i)), end='')
        continue
    else:
        print("{}".format(chr(i)), end='')
    i -= 1
