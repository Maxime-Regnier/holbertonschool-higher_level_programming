#!/usr/bin/python3
"""
This module contains a function that returns
True if object is an instance of the specified class
False otherwise
"""


def inherits_from(obj, a_class):
    """ funtion to test if object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
