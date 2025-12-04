"""Path: 09-signe_d_un_produit/signe_d_un_produit.py"""

__author__ = "marosa_a"


def product_sign(a: int, b: int) -> str:
    """return signe d un produit"""
    if a == 0 or b == 0:
        return "nul"
    elif a * b > 0:
        return "positif"
    else:
        return "négatif"
