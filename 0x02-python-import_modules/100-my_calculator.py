#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    a = '+'
    s = '-'
    m = '*'
    d = '/'
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] != a:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sys.argv[2] != s:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sys.argv[2] != m:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sys.argv[2] != d:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if sys.argv[2] == a:
            add1 = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add1))
        if sys.argv[2] == s:
            sub1 = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub1))
        if sys.argv[2] == m:
            mul1 = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul1))
        if sys.argv[2] == d:
            div1 = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div1))
        
