#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in len(matrix):
        for j in len(matrix[i]):
            if j == 2:
                print("{}{}".format(matrix[i][j], "\n"))
            else:
                print("{}".format(matrix[i][j]), end=' ')
