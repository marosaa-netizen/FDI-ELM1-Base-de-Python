"""recuperation du dernier element.py"""

__author__ = "marosa_a"


def last_element(seq) -> any:  # type: ignore
    """recuperation du dernier élément"""
    if len(seq) == 0:
        return None
    return seq[-1]
