"""Module pour calculer la somme des chiffres d'un nombre entier."""

__author__ = "marosa_a"


def sum_of_digits(n: int) -> int:
    """Retourne la somme des chiffres d'un entier n."""
    n = abs(n)
    return sum(int(digit) for digit in str(n))
