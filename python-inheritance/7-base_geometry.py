#!/usr/bin/python3
""" Document containing the BaseGeometry class """


class BaseGeometry:
    """ Class that manages geometry parameters """
    def area(self):
        """ Function that handles exceptions for air calculation """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
