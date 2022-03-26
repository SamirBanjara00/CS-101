import stdio
import sys

# nth input for number from the Fibonacci sequence
n = int(sys.argv[1])

# stores values
a = 0
b = 1
i = 3

# as long as I is less than or equal to n, then a will store the value of 1-0, and b will store the value 1+0
# sequentially. Then we set increment for i by 1 until i equal n (which is the nth number.
while i <= n:
    a = b - a
    b = a + b
    i += 1
# output
stdio.writeln(b)
