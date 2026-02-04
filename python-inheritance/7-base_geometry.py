#!/usr/bin/python3
""" Module containing the BaseGeometry class. """


class BaseGeometry:
    """ BaseGeometry class: defines common geometry methods. """
    def area(self):
        """ Calculates the area of the shape. """
        raise Exception("area() is not implemented")
    

    def integer_validator(self, name, value):
        """ Validates that a value is a positive integer. """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
