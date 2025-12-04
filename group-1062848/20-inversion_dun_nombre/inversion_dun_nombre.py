"""inversion_dun_nombre.py"""

__author__ = "marosa_a"


def reverse_number(n: int) -> str:
    """inversion d'un nombre entier n."""
    if n < 0:
        return "-" + str(-n)[::-1]
    return str(n)[::-1]
