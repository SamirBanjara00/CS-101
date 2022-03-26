# Accepts k (int) as command-line argument and a sequence of strings from standard input; and writes
# the kth string from the end to standard output.

from arrayqueue import ArrayQueue
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])
    queue = ArrayQueue()
    while not stdio.isEmpty():
        s = stdio.readString()
        queue.enqueue(s)
    n = len(queue)
    for i in range(n - k):
        queue.dequeue()
    stdio.writeln(queue.peek())


if __name__ == '__main__':
    main()
