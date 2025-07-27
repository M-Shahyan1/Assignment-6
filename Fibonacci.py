"""
Displays Digits within Fibonacci's sequence as a list
"""


class Fibonacci:
    def __init__(self, digits):
        if not isinstance(digits, int):
            raise ValueError
        self.A = 0
        self.B = 1
        self.count = 0
        self.max_count = digits + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_count:
            logged_digit = self.A
            self.A, self.B = self.B, self.A + self.B
            self.count += 1
            return logged_digit

        else:
            raise StopIteration

