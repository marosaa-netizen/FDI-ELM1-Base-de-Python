"""Path: 08-categorie_d_age/categorie_d_age.py"""

__author__ = "marosa_a"


def age_category(age: int) -> str:
    """return categorie d age"""
    if age < 12:
        return "enfant"
    elif age < 18:
        return "ado"
    elif age < 70:
        return "adulte"
    else:
        return "senior"
