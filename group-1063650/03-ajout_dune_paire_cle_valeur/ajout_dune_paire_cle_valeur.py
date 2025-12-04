"""ajout d'une paire cle valeur.py"""

__author__ = "marosa_a"


def add_entry(d: dict, key, value) -> dict:
    """ajoute d'une paire cle valeur"""
    d[key] = value
    return d
