#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    range_n = len(my_list) - 1
    if idx < 0 or idx > range_n:
        return my_list
    else:
        del my_list[idx]
        return my_list
