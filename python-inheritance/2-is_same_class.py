#!/usr/bin/python3
"""
This module contains a function that returns
True if object is exactly an instance of the specified class
False otherwise
"""

def is_same_class(obj, a_class):
    """ funtion to test if object is exactly an instance of a class """
    if type(obj) is a_class:
        return True
    else:
        return False