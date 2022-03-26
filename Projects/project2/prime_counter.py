import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set count (number of primes <= n) to 0
count = 0

# for each i from [2, n]...
for i in range(2, n):

    # Set j (potential divisor of i) to 2.
    j = 2
    f = 1

    while j <= i / j:
        # As long as j is less than or equal to i / j...

        if i % j == 0:
            f = 0
            # If j divides i, break (i is not a prime).
            break

        # Increment j by 1.
        j += 1

    if f == 1:
        count += 1

stdio.writeln(count)
# Write count to standard output.
