"""Path: tri_de_trois_nombres_sans_sort__.py"""

__author__ = "marosa_a"


def sort_three_numbers(a: int, b: int, c: int) -> tuple:
    """return tri de trois nombre sans sort"""
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c
