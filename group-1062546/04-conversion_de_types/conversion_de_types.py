"""Path: 04-conversion_de_types/coversion_de_types.py"""

__author__ = "marosa_a"


def convert_type(value):
    """return conversion de types"""
    if isinstance(value, str):
        return int(value)
    elif isinstance(value, int):
        return str(value)
