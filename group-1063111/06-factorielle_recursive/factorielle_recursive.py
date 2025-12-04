"""factorielle_recursive.py"""

__author__ = "marosa_a"


def recursive_factorial(n: int) -> int:
    """factorielle récursive"""
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)
