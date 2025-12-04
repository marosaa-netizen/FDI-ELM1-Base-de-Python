"""recherche_d_un_element_dans_une_liste.py"""

__author__ = "marosa_a"


def contains(lst: list, elem) -> bool:
    """recherche si un élément est dans une liste"""
    for item in lst:
        if item == elem:
            return True
    return False
