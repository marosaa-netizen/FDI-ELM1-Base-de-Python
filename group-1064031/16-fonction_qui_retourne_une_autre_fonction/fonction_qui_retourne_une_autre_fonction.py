"""fonction qui retourne une autre fonction.py"""

__author__ = "marosa_a"


def make_power(n: int):
    """fonction qui retorune une autre fonction"""

    def power(x: int) -> int:
        return x**n

    return power
