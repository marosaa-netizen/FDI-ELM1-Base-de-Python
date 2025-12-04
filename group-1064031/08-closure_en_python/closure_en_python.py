"""closure_en_python.py"""

__author__ = "marosa_a"


def make_adder(x: int):
    """closure qui ajoute un nombre x à un autre nombre"""

    def adder(y: int) -> int:
        return x + y

    return adder
