import stdio
import sys

# accepts t(float), v(float) as command line arguments
t = float(sys.argv[1])
v = float(sys.argv[2])

# function that calcuates weather
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# if elif else loop. Checks t and v.
if t > 50:
    stdio.writeln('Value of t must be <= 50 F')

elif v <= 3:
    stdio.writeln('Value of v must be > 3 mph')

else:
    stdio.writeln(w)
