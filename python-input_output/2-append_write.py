#!/usr/bin/python3
"""Append a string to a UTF-8 text file."""
def append_write(filename="", text=""):    
    """Append text to a UTF-8 file and return the number of characters added."""

    with open (filename, "a", encoding="utf-8") as f:
        chars_written = f.write(text)
        return chars_written