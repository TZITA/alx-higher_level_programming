#!/usr/bin/python3
import hidden_4
a = dir(hidden_4)
n = len(a) - 1
for i in range(0, n):
    e = a.[i]
    if e.startswith("__"):
        continue
    else:
        print("{}".format(e))
