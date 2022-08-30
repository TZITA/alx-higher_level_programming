#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if j == 2:
                print("{:d}{}".format(matrix[i][j], "\n"))
            else:
                print("{}".format(matrix[i][j]), end=" ")
