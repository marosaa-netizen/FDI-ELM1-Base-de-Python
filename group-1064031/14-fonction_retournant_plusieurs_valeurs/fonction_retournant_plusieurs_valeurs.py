"""fonction retournant plusieurs valeurs.py"""

__author__ = "marosa_a"


def sum_and_product(a: int, b: int) -> tuple:
    """fonction retournant plusieurs valeurs"""
    somme = a + b
    produit = a * b
    return somme, produit
