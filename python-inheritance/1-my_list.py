#!/usr/bin/python3
"""
This module defines a class MyList inherits from the built-in list class.
"""

class MyList(list):
    """
    MyList is a subclass of list providing a method
    to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without
        modifying the original list.
        """
        print(sorted(self))
