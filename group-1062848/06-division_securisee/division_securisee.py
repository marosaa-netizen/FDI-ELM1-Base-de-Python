"""Path: 06-division_securisee/division_securisee.py"""

__author__ = "marosa_a"

from typing import Union


def safe_divide(a: int, b: int) -> Union[float, str]:
    """Retourne la division sécurisée."""
    if b == 0:
        return "Erreur : division par zéro"
    return a / b
