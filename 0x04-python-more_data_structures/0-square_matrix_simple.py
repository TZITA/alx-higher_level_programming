#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cp_matrix = matrix.copy()
    sqlist = [[row[i] for row in cp_matrix] for i in range(len(matrix))]
    for j in range(len(sqlist)):
        for k in range(len(sqlist[j])):
            sqlist[j][k] *= sqlist[j][k]
    return sqlist
