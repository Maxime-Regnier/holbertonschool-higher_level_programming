#!/usr/bin/python3
"""
This module contains a function matrix_divided(matrix, div)
that divides all elements of a matrix by div and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix by div
    and returns a new matrix with results rounded to 2 decimals.
    """
    # Vérification de matrix
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification de div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création de la nouvelle matrice
    return [[round(num / div, 2) for num in row] for row in matrix]
