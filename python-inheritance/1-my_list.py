#!/usr/bin/python3
"""
This module defines a MyList class inheriting from the built-in list class.
"""


class MyList(list):
    """
    MyList is a subclass of list providing a method
    to print the list sorted in ascending order.
    """

    def __str__(self):
        """ We transform the instance (self) into a standard list,
        then into a string to fit the expected format. """
        return super().__str__()

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without
        modifying the original list.
        """
        print(sorted(self))
