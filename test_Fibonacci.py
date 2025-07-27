"""
Tests the Fibonacci module
"""
import pytest
from Fibonacci import Fibonacci

def test_Fibonacci_integer():
    with pytest.raises(ValueError):
        Fibonacci('Moon')

