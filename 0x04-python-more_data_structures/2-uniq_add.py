#!/usr/bin/python3
def uniq_add(my_list=[]):
    aset = set(my_list)
    alist = list(aset)
    sum1 = 0
    for i in range(0, len(alist)):
        sum1 += int(alist[i])
    return sum1
