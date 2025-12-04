"""fibonacci_recursif.py"""

__author__ = "marosa_a"


def fibonacci(n: int) -> int:
    """fibonacci récursif"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
