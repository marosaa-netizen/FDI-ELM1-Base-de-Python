"""tuple acceder a un element.py"""

__author__ = "marosa_a"


def get_tuple_element(tpl: tuple, index: int):
    """Retourne un élément du tuple ou None si l'index est invalide"""
    try:
        return tpl[index]
    except IndexError:
        return None
