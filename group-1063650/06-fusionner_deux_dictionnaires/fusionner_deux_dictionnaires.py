"""fusionner deux dictionnaires.py"""

__author__ = "marosa_a"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """retourne la fusion de deux dictionnaires"""
    merged_dict = d1.copy()
    merged_dict.update(d2)
    return merged_dict
