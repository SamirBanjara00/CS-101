# An immutable data type to represent a complex number using cartesian coordinates.

import math
import stdio


class Complex:
    # Constructs a complex number given its cartesian coordinates.
    def __init__(self, re=0.0, im=0.0):
        self.re = re  # the real part
        self.im = im  # the imaginary part

    # Returns the real part of this complex number.
    def re(self):
        return self.re

    # Returns the imaginary part of this complex number.
    def im(self):
        return self.im

    # Returns the conjugate of this complex number.
    def conjugate(self):
        return Complex(self.re, -self.im)

    # Returns the sum of this and the other complex number.
    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return Complex(re, im)

    # Returns the product of this and the other complex number.
    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return Complex(re, im)

    # Returns the magnitude of this complex number.
    def __abs__(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    # Returns True if this and other denote the same complex number, and False otherwise.
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    # Returns a string representation of this complex number.
    def __str__(self):
        SUFFIX = 'i'
        if self.im == 0:
            return str(self.re)
        elif self.re == 0:
            return str(self.im) + SUFFIX
        elif self.im < 0:
            return str(self.re) + ' - ' + str(-self.im) + SUFFIX
        else:
            return str(self.re) + ' + ' + str(self.im) + SUFFIX


# Unit tests the data type.
def _main():
    a = Complex(5.0, -6.0)
    b = Complex(3.0, 4.0)
    stdio.writeln("a       = " + str(a))
    stdio.writeln("b       = " + str(b))
    stdio.writeln("conj(a) = " + str((a.conjugate())))
    stdio.writeln("a + b   = " + str(a + b))
    stdio.writeln("a * b   = " + str(a * b))
    stdio.writeln("|b|     = " + str(abs(b)))


if __name__ == '__main__':
    _main()
