# An immutable data type that represents a profile of a string, as a d-dimensional unit vector.

from vector import Vector
import stdarray
import stdio
import sys


class Sketch:
    # Constructs a new sketch which is a profile of text, as a d-dimensional unit vector.
    # Component i of the vector indicates how many k-grams in the text hash to i.
    def __init__(self, text, k, d):
        freq = stdarray.create1D(d, 0)
        for i in range(len(text) - k + 1):
            kgram = text[i:i + k]
            h = hash(kgram)
            freq[abs(h % d)] += 1
        vector = Vector(freq)
        self.sketch = vector.direction()  # string profile as a d-dimensional unit vector

    # Returns the similarity measure between this and the other sketch, as a number between 0 and 1.
    # The value 0 indicates that the sketches are dissimilar, and 1 indicates that they are similar.
    def similarTo(self, other):
        return self.sketch.dot(other.sketch)

    # Returns a string representation of this sketch.
    def __str__(self):
        return str(self.sketch)


# Unit tests the data type.
def _main():
    k = int(sys.argv[1])
    d = int(sys.argv[2])
    text = stdio.readAll()
    sketch = Sketch(text, k, d)
    stdio.writeln(sketch)


if __name__ == '__main__':
    _main()
