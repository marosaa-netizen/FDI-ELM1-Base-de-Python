"""Path: 12-multiplication_sans_/multiplication_sans_.py"""

__author__ = "marosa_a"


def multiply(a: int, b: int) -> int:
    """return multiplication sans"""
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        result = -result
    return result
