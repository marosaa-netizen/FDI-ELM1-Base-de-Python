"""extraction des elements pairs d'une liste.py."""

__author__ = "marosa_a"


def even_numbers(lst: list) -> list:
    """extraire les elements pairs d'une liste."""
    return [num for num in lst if num % 2 == 0]
