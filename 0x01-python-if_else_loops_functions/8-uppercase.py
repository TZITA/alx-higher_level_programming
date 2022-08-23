#!/usr/bin/python3
def uppercase(str):
    for i in range(0,len(str)):
        if 97 <= ord(str[i]) <= 122:
            m = chr(ord(str[i]) + 32)
            print("{}".format(m), end='')
        else:
            continue
    print("{}".format('\n'))
