#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("{}".format("Fizz"), sep=' ')
        elif i % 5 == 0:
            print("{}".format("Buzz"), sep=' ')
        elif i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), sep=' ')
        else:
            print("{}".format(i), sep=' ')
