"""
string_utils.py - Utility functions for string operations.
"""

def reverse_string(s):
    """Returns the reversed version of a string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome (ignoring case and spaces)."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
