#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""
def pascal_triangle(n):    
    """Return a list of lists representing Pascal's triangle of n rows."""

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(previous_row)):
            new_row.append(previous_row[j - 1] + previous_row[j])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle