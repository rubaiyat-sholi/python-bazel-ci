"""
test_math_utils.py - Unit tests for math utility functions.
"""

import pytest
from src.math_utils import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    
    # Testing division by zero
    with pytest.raises(ValueError):
        divide(5, 0)
