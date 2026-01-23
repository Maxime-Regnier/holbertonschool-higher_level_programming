#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ 
    Module that divides all elements of a matrix 
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

    # Nouvelle matrice
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
            new_matrix.append(new_row)

    return new_matrix