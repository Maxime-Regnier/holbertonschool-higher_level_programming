#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.
    Removes spaces at the beginning and end of each printed line.

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Caractères après lesquels on doit sauter
    separators = ['.', '?', ':']
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # extraire la portion de texte jusqu'au caractère
            line = text[start:i + 1].strip()
            print(line)
            print()  # première nouvelle ligne
            print()  # deuxième nouvelle ligne
            start = i + 1  # début du prochain segment

    # imprimer ce qui reste après le dernier séparateur
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
