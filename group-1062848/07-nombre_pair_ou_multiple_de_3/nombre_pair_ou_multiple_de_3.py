"""Path: nombre_pair_ou_multiple_de_3.py"""

__author__ = "marosa_a"


def check_number(n: int) -> str:
    """return nombre pair ou multiple de 3"""
    if n % 3 == 0:
        return "multiple de 3"
    elif n % 2 == 0:
        return "pair"
    else:
        return "rien de spécial"
