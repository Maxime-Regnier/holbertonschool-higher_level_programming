#!/usr/bin/python3
"""Module defines Student class."""
class Student:
    """Student with first_name, last_name, and age."""


    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of attributes; filter by attrs if list provided."""
        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered_dict[key] = getattr(self, key)
            return filtered_dict
        return self.__dict__