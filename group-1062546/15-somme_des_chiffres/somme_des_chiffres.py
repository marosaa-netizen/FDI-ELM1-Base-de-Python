"""Path: 15-somme_des_chiffres/somme_des_chiffres.py"""

__author__ = "marosa_a"


def sum_of_digits(n: int) -> int:
    """return somme des chiffres"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
