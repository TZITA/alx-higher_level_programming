#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    add1 = add(a, b)
    sub1 = sub(a, b)
    mul1 = mul(a, b)
    div1 = div(a, b)
    print("{} + {} = {}".format(a, b, add1))
    print("{} - {} = {}".format(a, b, sub1))
    print("{} * {} = {}".format(a, b, mul1))
    print("{} / {} = {}".format(a, b, div1))
