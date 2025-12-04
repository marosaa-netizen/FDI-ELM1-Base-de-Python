"""Path: annee_bissextile.py"""

__author__ = "marosa_a"


def is_leap_year(year: int) -> bool:
    """Return année bissextile"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
