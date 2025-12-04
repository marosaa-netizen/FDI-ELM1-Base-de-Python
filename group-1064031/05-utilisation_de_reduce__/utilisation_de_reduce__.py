"""utilisation_de reduce__.py"""

__author__ = "marosa_a"

from functools import reduce


def product(numbers: list) -> int:
    """utilisation de reduce"""
    return reduce(lambda x, y: x * y, numbers, 1)
