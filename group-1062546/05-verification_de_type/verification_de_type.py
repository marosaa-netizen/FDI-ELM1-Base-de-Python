"""Path: 05-verificationde_type/verification_de_type.py"""

__author__ = "marosa_a"


def get_type(value) -> str:
    """return verification de type"""
    return type(value).__name__
