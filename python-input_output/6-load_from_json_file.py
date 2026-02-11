#!/usr/bin/python3
"""
Module to load a Python object from a JSON file.
"""
import json
def load_from_json_file(filename):    
    """Load an object from a JSON file."""

    with open(filename, "r") as f:
        json.load(f)
        return json.load(f)