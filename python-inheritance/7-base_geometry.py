#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): Name of the parameter
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        # Ensure value is exactly int (bool excluded)
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
