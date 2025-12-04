"""16-factorielle_dun_nombre/factorielle_dun_nombre.py"""

__author__ = "marosa_a"


def factorial(n: int) -> int:
    """Calcule la factorielle d'un nombre n."""
    if n < 0:
        raise ValueError("Le nombre doit être positif ou nul")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
