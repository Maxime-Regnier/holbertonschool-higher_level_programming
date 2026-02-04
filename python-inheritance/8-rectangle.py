#!/usr/bin/python3
""" Module defining a Rectangle class that inherits from BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.
    
    Attributes:
    __width (int): Width of the rectangle (private)
    __height (int): Height of the rectangle (private)
    """
    
    def __init__(self, width, height):   
        """
        Initialize a Rectangle instance.
    
        Args:
            width (int): Width of the rectangle (must be positive integer)
            height (int): Height of the rectangle (must be positive integer)
        """
        self.integer_validator("width", width)    
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        """Return a readable string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)