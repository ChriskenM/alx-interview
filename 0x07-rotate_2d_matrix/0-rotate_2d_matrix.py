#!/usr/bin/python3
"""
Rotates a 2D matrix 90 degrees clockwise in-place.

Args:
    matrix: A 2D list representing the matrix to be rotated.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    This function performs a two-step rotation:
        1. Transpose the matrix: swap rows and columns.
        2. Reverse each row of the transposed matrix.

    Args:
        matrix: A 2D list representing the matrix to be rotated.
    """

    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

