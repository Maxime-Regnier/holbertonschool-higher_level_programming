#!/usr/bin/python3    
"""Writes a string to a UTF-8 text file and returns the number of characters written.
    
Args:
    filename (str): The name of the file
    text (str): The text to write

Returns:
    int: Number of characters written
"""
def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of characters written."""

    with open(filename, "w", encoding="utf-8") as f:
        chars_written = f.write(text)
        return chars_written