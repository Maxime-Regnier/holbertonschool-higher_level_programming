#!/usr/bin/python3
"""Reads a text file (UTF-8) and prints it to standard output."""


def read_file(filename=""):
    """Reads a text file and prints its content to standard output.

     Args:
            filename (str): The name of the file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
