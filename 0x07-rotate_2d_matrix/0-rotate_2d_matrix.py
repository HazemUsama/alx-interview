#!/usr/bin/python3
"""Rotate 2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix Function"""
    n: int = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(int(n / 2)):
            rev = n - j - 1
            matrix[i][j], matrix[i][rev] = matrix[i][rev], matrix[i][j]
