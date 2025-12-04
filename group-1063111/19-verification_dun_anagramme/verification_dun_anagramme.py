"""vérification d'un anagramme.py"""

__author__ = "marosa_a"


def is_anagram(word1: str, word2: str) -> bool:
    """vérification d'un anagramme"""
    return sorted(word1.lower()) == sorted(word2.lower())
