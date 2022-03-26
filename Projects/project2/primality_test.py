import stdio
import sys

# Accept n (int) as command-line argument

n = int(sys.argv[1])

# Set i (potential divisor of n) to 2.
i = 2
flag = 0
while i <= n // i:

    # As long as Igh is less than or equal to n / i...
    if n % i == 0:
        flag = 1
        # If i divides n, break (n is not a prime).
        break

        # Increment i by 1.
    i += 1

if n != 1 and flag == 0:
    stdio.writeln('True')

else:
    stdio.writeln('False')
