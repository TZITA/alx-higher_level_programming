#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cp_matrix = matrix.copy()
    for j in range(len(cp_matrix)):
        for k in range(len(cp_matrix[j])):
            cp_matrix[j][k] *= cp_matrix[j][k]
    return cp_matrix
