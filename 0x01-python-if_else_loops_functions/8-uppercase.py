#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        n = ord(str[i])
        if n <= 122 and n >= 97:
            m = chr(n + 32)
            print("{}".format(m), end='')
        else:
            continue
        i += 1
    print("{}".format('\n'))
