# An iterable data type to iterate over the first n numbers from the Fibonacci sequence.

import stdio
import sys


class FibonacciSequence:
    # Constructs a FibonacciSequence object given the length of the sequence.
    def __init__(self, n):
        self.n = n  # length of the sequence

    # Returns an iterator that iterates over the numbers in the sequence.
    def __iter__(self):
        self._a = -1  # previous number in the sequence
        self._b = 1  # current number in the sequence
        self._count = 0  # count of numbers iterated so far
        return self

    # Returns the next number in the sequence if there is one, and raises StopIteration
    # otherwise.
    def __next__(self):
        self._count += 1
        if self._count > self.n:
            raise StopIteration()
        temp = self._a
        self._a = self._b
        self._b += temp
        return self._b

    # Returns a string representation of this object.
    def __str__(self):
        s = ''
        for v in self:
            s += str(v) + ' '
        return s.strip()


# Unit tests the data type.
def _main():
    n = int(sys.argv[1])
    for v in FibonacciSequence(n):
        stdio.writeln(v)


if __name__ == '__main__':
    _main()
