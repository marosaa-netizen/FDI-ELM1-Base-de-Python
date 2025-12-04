"""Path: 11-jour_de_la_semaine/jour_de_la_semaine.py"""

__author__ = "marosa_a"


def day_of_week(n: int) -> str:
    """return jour de la semaine"""
    days = {
        1: "lundi",
        2: "mardi",
        3: "mercredi",
        4: "jeudi",
        5: "vendredi",
        6: "samedi",
        7: "dimanche"
    }
    return days.get(n, "Erreur, nombre invalide")
