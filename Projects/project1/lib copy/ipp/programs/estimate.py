# Accepts n (int), p (float), and trials (int) as command-line arguments; creates trials random
# n-by-n percolation systems with vacancy probability p; determines the fraction of them that
# percolates; and writes that fraction to standard output.

import percolation
import percolationio
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    stdio.writeln(evaluate(n, p, trials))


# Generates a random n-by-n percolation system with vacancy probability p and determines if the
# system percolates. Repeats trials times. Returns an estimate of the empirical percolation
# probability of such systems.
def evaluate(n, p, trials):
    count = 0
    for i in range(trials):
        isOpen = percolationio.random(n, p)
        isFull = percolation.flow(isOpen)
        if percolation.percolates(isFull):
            count += 1
    return count / trials


if __name__ == '__main__':
    main()
