#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        sum1 = 0
        sum2 = 0
        mul = []
        for i in range(len(my_list)):
            for j in range(len(my_list[0])):
                mul.append(my_list[i][j])
        for k in range(0, len(mul), 2):
            sum1 += (mul[k] * mul[k + 1])
            sum2 += mul[k + 1]
        return sum1/sum2
