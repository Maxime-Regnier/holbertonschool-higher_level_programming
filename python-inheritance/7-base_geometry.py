#!/usr/bin/python3
"""Module containing the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): Name of the variable
            value (any): Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
