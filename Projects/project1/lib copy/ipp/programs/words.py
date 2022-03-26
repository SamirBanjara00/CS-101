# An iterable data type to iterate over the words in a sentence.

import stdio
import sys


class Words:
    # Constructs a Words object from the given sentence.
    def __init__(self, sentence):
        self.words = sentence.split()  # words in the sentence

    # Returns an iterator to iterate over the words in a sentence.
    def __iter__(self):
        self._current = 0  # index of the current word
        return self

    # Returns the next word in the sentence if there is one, and raises StopIteration otherwise.
    def __next__(self):
        if self._current == len(self.words):
            raise StopIteration
        word = self.words[self._current]
        self._current += 1
        return word

    # Returns a string representation of this object.
    def __str__(self):
        s = ''
        for v in self:
            s += str(v) + ' '
        return s.strip()


# Unit tests the data type.
def _main():
    sentence = sys.argv[1]
    words = Words(sentence)
    for word in words:
        stdio.writeln(word)


if __name__ == '__main__':
    _main()
