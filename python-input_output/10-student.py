#!/usr/bin/python3
class Student:
    """Defines a student with first_name, last_name, and age."""


    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance."""
        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered_dict[key] = getattr(self, key)
            return filtered_dict
        return self.__dict__