#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle (positive integer)
            height (int): height of the rectangle (positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description for print() and str()."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
