import math
import stdio
import sys

# input
x1 = math.radians(float(sys.argv[1]))
y1 = math.radians(float(sys.argv[2]))
x2 = math.radians(float(sys.argv[3]))
y2 = math.radians(float(sys.argv[4]))

# formula
d = math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# formula was too long, so I divided it
e = 6359.83 * d

# output
stdio.writeln(str(e))

# removed math.radians from indv variables. put it at begining of string
# ok im getting fustrated while doing this. I belive i have the right code,
# but its not working. The math is not working.
# found solution i had d = math.degrees(d), but this reconverted the radins to degrees.
