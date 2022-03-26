# A library that implements linear search.

from instream import InStream
import stdio
import sys


# Returns the index of key in the array a, or -1.
def indexOf(a, key):
    for i in range(len(a)):
        if key == a[i]:
            return i
    return -1


# Unit tests the library.
def _main():
    inStream = InStream(sys.argv[1])
    whiteList = inStream.readAllInts()
    while not stdio.isEmpty():
        key = stdio.readInt()
        if indexOf(whiteList, key) == -1:
            stdio.writeln(key)


if __name__ == '__main__':
    _main()
