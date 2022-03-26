# A library that implements binary search.

from instream import InStream
import stdio
import sys


# Returns the index of key in the sorted array a, or -1.
def indexOf(a, key):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


# Unit tests the library.
def _main():
    inStream = InStream(sys.argv[1])
    whiteList = inStream.readAllInts()
    whiteList.sort()
    while not stdio.isEmpty():
        key = stdio.readInt()
        if indexOf(whiteList, key) == -1:
            stdio.writeln(key)


if __name__ == '__main__':
    _main()
