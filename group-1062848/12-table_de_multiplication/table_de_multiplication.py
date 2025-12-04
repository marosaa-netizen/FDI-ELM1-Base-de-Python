"""Path: 12-table_de_multiplication/table_de_multiplication.py"""

__author__ = "marosa_a"


def multiplication_table(n: int) -> list:
    """Retourne la table de multiplication dun nombre sous forme de liste."""
    return [n * i for i in range(1, 11)]
