"""fonction_recursive___factorielle.py"""

__author__ = "marosa_a"


def factorial(n: int) -> int:
    """fonction recursive factorielle"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
