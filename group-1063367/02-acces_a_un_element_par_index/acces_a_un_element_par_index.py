"""acces a un element par index.py"""

__author__ = "marosa_a"


def get_element(lst: list, index: int):
    """return un element par index"""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None
