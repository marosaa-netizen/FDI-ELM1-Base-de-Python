"""decorateur simple.py"""

__author__ = "marosa_a"


def debug(func):
    """decorateur simple"""

    def wrapper():
        print("Début")
        func()
        print("Fin")

    return wrapper
