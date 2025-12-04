"""chifre_le_plus_grand.py"""

__author__ = "marosa_a"


def max_digit(n: int) -> int:
    """Retourne le chiffre le plus grand dans un entier n."""
    n = abs(n)
    return max(int(digit) for digit in str(n))
