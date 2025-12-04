"""utilisation de filter__.py"""

__author__ = "marosa_a"


def filter_even(numbers: list) -> list:
    """utilisation de filter"""
    return list(filter(lambda x: x % 2 == 0, numbers))
