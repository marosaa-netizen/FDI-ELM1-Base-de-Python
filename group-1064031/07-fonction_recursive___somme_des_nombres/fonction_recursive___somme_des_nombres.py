"""fonction_recursive somme des nombres.py"""

__author__ = "marosa_a"


def sum_recursive(n: int) -> int:
    """fonction recursive somme des nombres"""
    if n < 0:
        raise ValueError("Sum is not defined for negative integers.")
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
