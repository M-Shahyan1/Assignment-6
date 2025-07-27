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

def test_Fibonacci_two():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_Fibonacci_4():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]
