"""Path: 19-signe_dun_nombre/signe_dun_nombre.py"""

__author__ = "marosa_a"


def sign(n: int) -> int:
    """return signe dun nombre"""
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
