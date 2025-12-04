"""acces a une valeur.py"""

__author__ = "marosa_a"


def get_value(d: dict, key: str):
    """acces a une valeur par sa cle"""
    return d.get(key)
