"""fusion de listes.py"""

__author__ = "marosa_a"


def merge_lists(list1: list, list2: list) -> list:
    """fusionne deux listes"""
    merged = list1 + list2
    result = []
    for item in merged:
        if item not in result:
            result.append(item)
    return result
