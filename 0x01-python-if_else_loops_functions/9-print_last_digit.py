#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num1 = number * (-1)
        num = num1 % 10
        return str(num)
    else:
        num = number % 10
        print("{}".format(num), end='')
