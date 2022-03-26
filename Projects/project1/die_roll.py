import stdio
import stdrandom
import sys

# input
n = int(sys.argv[1])

# std.random.uniformInt generates two numbers between 1, n randomly.  Functions
die1 = stdrandom.uniformInt(1, n+1)
die2 = stdrandom.uniformInt(1, n+1)

# Output need to add the result of die1 and die2 to calculate sum
stdio.writeln(die1 + die2)
