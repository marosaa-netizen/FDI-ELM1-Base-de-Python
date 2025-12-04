"""Path: 16-factorielle_sans_math_factorial__/
factorielle_sans_math_factorial__.py"""

__author__ = "marosa_a"


def factorial(n: int) -> int:
    """return factorielle sans math factorial"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
