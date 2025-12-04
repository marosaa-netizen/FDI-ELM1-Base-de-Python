"""fonction qui modifie une variable globale.py"""

__author__ = "marosa_a"

global_var = 0


def modify_global():
    """fonction qui modifie une variable globale"""
    global global_var
    global_var = 10
    return str(global_var)
