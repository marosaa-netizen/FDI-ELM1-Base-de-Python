"""suppression d'une cle.py"""

__author__ = "marosa_a"


def remove_key(d: dict, key) -> dict:
    """supprime une cle du dictionnaire"""
    if key in d:
        del d[key]
    return d
