#!/usr/bin/env python3
import json
def serialize_and_save_to_file(data, filename):    
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)
