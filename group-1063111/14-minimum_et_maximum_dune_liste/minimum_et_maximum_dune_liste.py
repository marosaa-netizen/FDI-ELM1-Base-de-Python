"""minimum et maximum d'une liste.py"""

__author__ = "marosa_a"


def min_max(numbers: list) -> tuple:
    """minimum et maximum d'une liste"""
    if not numbers:
        return (None, None)
    return (min(numbers), max(numbers))
