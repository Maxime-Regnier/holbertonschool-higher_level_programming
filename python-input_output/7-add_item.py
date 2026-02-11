#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to add_item.json.

- Uses save_to_json_file from 5-save_to_json_file.py
- Uses load_from_json_file from 6-load_from_json_file.py
- Creates add_item.json if it does not exist
"""
import sys
from pathlib import Path
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)
args = sys.argv[1:]
filename = "add_item.json"
if Path(filename).exists():
    my_list = load_from_json_file(filename)
else:
    my_list = []
my_list.extend(args)
save_to_json_file(my_list, filename)