"""verification de palindromes.py"""

__author__ = "marosa_a"


def is_palindrome(word: str) -> bool:
    """verification de palindrome"""
    word = word.lower()
    return word == word[::-1]
