"""verifier si_un_ensemble_est_un_sous_ensemble.py"""

__author__ = "marosa_a"


def is_subset(s1: set, s2: set) -> bool:
    """verifie si un ensemble est un sous-ensemble"""
    return s1.issubset(s2)
