#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = matrix.copy()
    for j in range(len(matrix1)):
        for k in range(len(matrix1[j])):
            matrix1[j][k] *= matrix1[j][k]
    return matrix1
