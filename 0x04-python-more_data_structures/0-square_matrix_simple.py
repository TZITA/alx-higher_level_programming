#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cp_matrix = matrix.copy()
    listoflist = []
    for i in range(len(cp_matrix)):
        listoflist.append(cp_matrix[i])
    for j in range(len(listoflist)):
        for k in range(len(listoflist[j])):
            listoflist[j][k] *= listoflist[j][k]
    return listoflist
