import math
import stdio
import sys

# inputs
O1 = math.radians(float(sys.argv[1]))
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# formula
O2 = math.degrees(math.asin((n1 * math.sin(O1)) / n2))

# output
stdio.writeln(str(O2))

# orginally had O2 = math.degrees(O1 * (n2 / n1))
# fixed the formula imto math.degrees(math.asin((n1 * math.sin(O1)) / n2))
