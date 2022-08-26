#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    range_n = len(my_list) - 1
    
    if idx < 0 or idx > range_n:
        return my_list.copy()
    else:
        cp_list = my_list.copy()
        cp_list[idx] = element
        return cp_list
