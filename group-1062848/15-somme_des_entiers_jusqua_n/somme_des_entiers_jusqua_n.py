"""Path: 15-somme_des_entiers_jusqua_n/somme_des_entiers_jusqua_n.py"""

__author__ = "marosa_a"


def sum_up_to(n: int) -> int:
    """Retourne la somme des entiers de 1 à n."""
    return n * (n + 1) // 2
