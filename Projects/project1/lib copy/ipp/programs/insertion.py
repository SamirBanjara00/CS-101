# This library implements insertion sort.

import stdio
import sys


# Sorts the specified array according to the natural ordering of its objects, or according to
# the order induced by key, if one is specified.
def sort(a, key=None):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            v, w = a[j], a[j - 1]
            if key:
                v, w = key(v), key(w)
            if v >= w:
                break
            _exchange(a, j, j - 1)


# Exchanges two objects in the specified array.
def _exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Unit tests the library.
def _main():
    a = stdio.readAllStrings()
    if sys.argv[1] == '-':
        sort(a, key=lambda x: x.lower())
    elif sys.argv[1] == '+':
        sort(a)
    else:
        raise Exception('Illegal command-line argument')
    for s in a:
        stdio.write(s + ' ')
    stdio.writeln()


if __name__ == '__main__':
    _main()
