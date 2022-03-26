import stdio
import sys

# input m1 and m2 and r as float command line arguments
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# assign math function to var g
g = 6.674 * (10 ** -11)

# compute f using var g, and command line input var m1, m2, r
f = g * ((m1 * m2) / (r ** 2))

# print string f, switched float to string
stdio.writeln(str(f))

# easy
