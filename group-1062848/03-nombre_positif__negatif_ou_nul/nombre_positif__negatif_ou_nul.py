"""Path: 03-nombre_positif__negatif_ou_nul/nombre_positif__negatif_ou_nul.py"""

__author__ = "marosa_a"


def number_sign(n: int) -> str:
    """return nombre positif negatif ou nul"""
    if n > 0:
        return "positif"
    elif n < 0:
        return "négatif"
    else:
        return "nul"
