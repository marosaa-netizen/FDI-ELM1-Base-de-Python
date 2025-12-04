"""supprimer_un_element_dun_ensemble.py"""

__author__ = "marosa_a"


def remove_from_set(s: set, elem) -> set:
    """supprime un element d'un ensemble"""
    s.discard(elem)
    return s
