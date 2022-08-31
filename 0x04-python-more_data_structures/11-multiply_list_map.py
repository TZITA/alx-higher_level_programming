#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    cp_list = my_list.copy()
    new_list = list(map(lambda x: x * number, cp_list))
    return new_list
