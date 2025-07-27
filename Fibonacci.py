"""
Displays Digits within Fibonacci's sequence as a list
"""

class Fibonacci:
    def __init__(self, digits):
        if not isinstance(digits, int):
            raise ValueError