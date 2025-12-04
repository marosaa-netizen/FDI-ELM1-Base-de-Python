"""suppresion dun element.py"""

__author__ = "marosa_a"


def remove_element(lst: list, elem) -> list:
    """Supprime un élément spécifique d'une liste s'il existe"""
    if elem in lst:
        lst.remove(elem)
    return lst
