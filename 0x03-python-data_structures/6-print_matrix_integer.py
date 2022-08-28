#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_a = len(matrix[0])
    len_b = len(matrix)
    for i in range(len_b):
        for j in range(len_a):
            if j == len_a - 1:
                print("{:d}{}".format(matrix[i][j], "\n"))
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
