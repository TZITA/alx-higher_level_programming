#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 2:
    print("{} argument:".format(n - 1))
    print("1: {}".format(str(sys.argv[1])))
elif n == 1:
    print("{} arguments.".format(n - 1))
else:
    print("{} arguments:".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, str(sys.argv[i])))
