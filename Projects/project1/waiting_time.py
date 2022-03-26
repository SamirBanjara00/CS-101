import math
import stdio
import sys

# inputs
lam = float(sys.argv[1])
t = float(sys.argv[2])

# function
p = math.exp(-lam * t)

# output
stdio.writeln(str(p))
