"""
test_string_utils.py - Unit tests for string utility functions.
"""

import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True  # Should ignore spaces and case

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0
