#!/usr/bin/python3
def element_at(my_list, idx):
    range_n = len(my_list) - 1
    if idx < 0 or idx > range_n:
        return None
    else:
        elem = my_list[idx]
        return elem
        
