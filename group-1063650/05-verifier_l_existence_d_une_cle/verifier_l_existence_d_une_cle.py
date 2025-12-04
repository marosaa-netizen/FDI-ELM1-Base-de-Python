"""verifier l'existence d'une cle.py"""

__author__ = "marosa_a"


def key_exists(d: dict, key) -> bool:
    """verifie l'existence d'une cle dans le dictionnaire"""
    return key in d
