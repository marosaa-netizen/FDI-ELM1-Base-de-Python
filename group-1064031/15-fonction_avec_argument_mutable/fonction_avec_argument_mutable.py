"""fonction avec argument mutable.py"""

__author__ = "marosa_a"


def add_to_list(item, lst=None) -> list:
    """fonction avec argument mutable"""
    if lst is None:
        lst = []
    lst.append(item)
    return lst
