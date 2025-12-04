"""nombre doccurrences dun element.py"""

__author__ = "marosa_a"


def count_occurrences(lst: list, elem) -> int:
    """nombre doccurrences dun element"""
    count = 0
    for item in lst:
        if item == elem:
            count += 1
    return count
