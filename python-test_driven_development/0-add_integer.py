#!/usr/bin/python3
"""
This module contains the function add_integer(a, b)
that adds two integers and returns the result.
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Floats are converted to integers before addition.
    
    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: If a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
