"""Path: 13-verification_de_palindrome/verification_de_palindrome.py"""

__author__ = "marosa_a"


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (case-insensitive)"""
    s = s.lower()
    return s == s[::-1]
