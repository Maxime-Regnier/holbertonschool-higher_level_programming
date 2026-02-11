#!/usr/bin/python3
"""Module that converts Python objects to JSON strings."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object as a string."""
    return json.dumps(my_obj)
