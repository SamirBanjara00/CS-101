import stdio
import sys

# accepts command line inputs
n = int(sys.argv[1])
k = int(sys.argv[2])

# starts sum at 0
total = 0

# within the range from 1 to nth number
for i in range(1, n+1):

    # total of n^k from 1 to nth number
    total += i ** k

# output
stdio.writeln(total)
