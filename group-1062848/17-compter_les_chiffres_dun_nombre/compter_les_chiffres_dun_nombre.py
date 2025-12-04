"""compter_les_chiffres_dun_nombre.py"""

__author__ = "marosa_a"


def count_digits(n: int) -> int:
    """Compte le nombre de chiffres dans un nombre entier n."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
