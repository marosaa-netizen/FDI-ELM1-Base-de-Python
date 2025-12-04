"""suppression_des_valeurs_nulles.py"""

__author__ = "marosa_a"


def remove_none(lst: list) -> list:
    """suppresse les valeurs nulles"""
    return [x for x in lst if x is not None]
