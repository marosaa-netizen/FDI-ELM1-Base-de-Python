"""Path: 05-comparaison_de_trois_nombres/comparaison_de_trois_nombres.py"""

__author__ = "marosa_a"


def max_of_three(a: int, b: int, c: int) -> int:
    """Retourne le plus grand des trois nombres."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
