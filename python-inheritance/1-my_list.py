#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """MyList class inherits from list and adds a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
