"""utilisation de sorted avec key.py"""

__author__ = "marosa_a"


def sort_tuples(lst: list) -> list:
    """utilisation de sorted avec key"""
    return sorted(lst, key=lambda x: x[1])
