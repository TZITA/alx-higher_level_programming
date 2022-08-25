#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    sum1 = 0
    for i in range(1, n):
        sum1 += int(sys.argv[i])
    print("{}".format(sum1))
