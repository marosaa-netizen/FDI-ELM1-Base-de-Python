"""Path: 14-nombre_premier/nombre_premier.py"""

__author__ = "marosa_a"


def is_prime(n: int) -> bool:
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
