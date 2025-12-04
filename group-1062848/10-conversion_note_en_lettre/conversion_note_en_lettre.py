"""Path: 10-conversion_note_en_lettre/conversion_note_en_lettre.py"""

__author__ = "marosa_a"


def grade_conversion(score: int) -> str:
    """Convertit une note numérique en lettre."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
