#!/usr/bin/python3
"""Module defining a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square (positive integer)
        """
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle constructor with width=size, height=size
        super().__init__(size, size)
