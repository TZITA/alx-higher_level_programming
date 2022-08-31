#!/usr/bin/python3
def uniq_add(my_list=[]):
    item = my_list[0]
    taddl = [my_list[0]]
    sum1 = 0
    for i in range(0, len(my_list)):
        if my_list[i] != item:
            taddl.append(my_list[i])
    for j in range(0, len(taddl)):
        sum1 += int(my_list[j])
    return sum1
