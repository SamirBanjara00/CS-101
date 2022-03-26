import stdio
import stdrandom
import sys

# Accept a (int) and b (int) as command-line arguments.
a = int(sys.argv[1])
b = int(sys.argv[2])

# Set r to a random integer between a and b, obtained by calling stdrandom.uniformInt().
r = stdrandom.uniformInt(a, b)

# Write r to standard output.
stdio.writeln(r)

# had to google the function std.random.uniformInt() to understand what it did
# without adjustments the funtion stdrandom.uniformInt(a,b) return a
# random integer uniformly in [a,b), where a is inclusive of the int provided and will output a
# and returned rand int will never output b  because it is excluive
