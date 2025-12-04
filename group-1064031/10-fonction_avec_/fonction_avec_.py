"""fonction_recursive___factorielle.py"""

__author__ = "marosa_a"


def greet(**kwargs) -> str:
    """fonction recursive factorielle"""
    name = kwargs.get("name", "Inconnu")
    age = kwargs.get("age", "inconnu")
    return f"{name} a {age} ans."
