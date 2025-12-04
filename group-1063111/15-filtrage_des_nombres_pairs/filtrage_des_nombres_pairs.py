"""filtrage des nombres pairs.py"""

__author__ = "marosa_a"


def filter_even(numbers: list) -> list:
    """filtre les nombres pairs dans une liste"""
    return [number for number in numbers if number % 2 == 0]
