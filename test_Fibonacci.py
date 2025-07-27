"""
Tests the Fibonacci module
"""
import pytest
from Fibonacci import Fibonacci

def test_Fibonacci_integer():
    with pytest.raises(ValueError):
        Fibonacci('Moon')

def test_Fibonacci_zero():
    assert list(Fibonacci(0)) == [0]

def test_Fibonacci_one():
    assert list(Fibonacci(1)) == [0, 1]

