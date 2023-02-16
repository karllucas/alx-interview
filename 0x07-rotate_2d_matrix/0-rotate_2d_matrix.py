#!/usr/bin/python3
"""
0-rotate_2d_matrix
"""


def rotate_2d_matrix(mat):
    """
    Rotate 2d matrix 90 deg.
    """
    if not len(mat) or len(mat) != len(mat[0]):
        return
    n = len(mat)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for i in range(first, last):
            top = mat[first][i]
            mat[first][i] = mat[last - offset][first]
            mat[last - offset][first] = mat[last][last - offset]
            mat[last][last - offset] = mat[i][last]
            mat[i][last] = top
            offset += 1
