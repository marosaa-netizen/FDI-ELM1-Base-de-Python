"""Path: 13-verification_d_un_triangle/verification_d_un_triangle.py"""

__author__ = "marosa_a"


def is_triangle(a: int, b: int, c: int) -> bool:
    """return verification d un triangle"""
    return a + b > c and a + c > b and b + c > a
